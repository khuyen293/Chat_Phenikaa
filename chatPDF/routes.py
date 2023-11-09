from chatPDF import app, db, bcrypt 
from flask import render_template, redirect, url_for, request, flash
from chatPDF.models import User, Topic, Conversation
from datetime import datetime, timedelta

from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.storage.file_system import LocalFileStore
from langchain.embeddings.cache import CacheBackedEmbeddings
from flask import jsonify

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# Lấy giá trị của biến môi trường từ tệp .env
openai_api_key = os.getenv('OPENAI_API_KEY')

# Multiple PDFs
def get_pdfs_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        text += get_pdf_text(pdf)
    return text

# Single PDF
def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    fs = LocalFileStore("./chatPDF/cache/")
    underlying_embeddings = OpenAIEmbeddings()
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, fs, namespace=underlying_embeddings.model
    )
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding= cached_embedder)
    return vectorstore

prompt = """You are an AI assistant created by Phenikaa University to answer questions about the university and have friendly conversations with students. 
Your goal is to be helpful, exaclly. 
If you can't find the information, say you don't know. Don't try to make up answers.
Please answer in maximum 100 words.
Please using Vietnamese"""

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(temperature= 0.5, model_name= "gpt-3.5-turbo-16k")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain

pdf = get_pdfs_text(["./chatPDF/pdf/Thoi khoa bieu Tuan SHCD K15- Ngày 15.9.2021.pdf","./chatPDF/pdf/Thông báo về việc xin miễn giảm và nộp học phí .pdf", "./chatPDF/pdf/Tb_ra_vao_cong.pdf", "./chatPDF/pdf/ctdtict1-1.pdf"])
chunks = get_text_chunks(pdf)
vec = get_vectorstore(chunks)

    

def get_current_date():
    return {'current_date': datetime.today().strftime('%d')}

app.context_processor(get_current_date) 

# Hàm chuyển đổi tên người dùng
def convert_name_to_abbreviation(name):
    words = name.split()
    abbreviation = ""

    if len(words) > 1:
        abbreviation = words[0][0].upper() + words[-1][0].upper()
    elif len(words) == 1:
        abbreviation = words[0][0].upper()

    return abbreviation


@app.route('/')
@app.route('/home')
def home():  
    return render_template('home_chatbot.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            next_page = request.args.get('next')
            if(not user.topics):
                topic = Topic(user_id = user.id)
                db.session.add(topic)
                db.session.commit()
            return redirect(url_for('admin', user=user.id)) if user.role == 'admin' else redirect(url_for('baseuser', user=user.id, topic = user.topics[-1].id))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')
    
@app.route('/sigup', methods=["GET", "POST"])
def sigup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Account already exists', 'warning')
        elif password != confirm_password:
            flash('Password does not match', 'warning')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
    return render_template('sigup.html')

@app.route('/baseuser')
def baseuser():
    id_user = request.args.get('user')
    id_topic = request.args.get('topic')
    user = User.query.filter_by(id=id_user).first()
    new_name = convert_name_to_abbreviation(user.username)
    topic = Topic.query.filter_by(id=id_topic).first()
    return render_template('baseuser.html', user=user, topic = topic, new_name = new_name)

@app.route('/usernotaccount')
def usernotaccount():
    return render_template('usernotaccount.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add_topic', methods=['POST'])
def add_topic():
    data = request.get_json()
    if 'user_id' in data:
        user_id = data['user_id']
        new_topic = Topic(user_id=user_id)
        db.session.add(new_topic)
        db.session.commit()
    else:
        return jsonify({'error': 'Dữ liệu ngu không hợp lệ'}), 400

@app.route('/rename_topic', methods=['POST'])
def rename_topic():
    
    data = request.get_json()
    if 'updatedTitle' in data:
        updatedTitle = data['updatedTitle']
        topic_id = data['topic_id']
        getTopic = Topic.query.filter_by(id = topic_id).first()
        getTopic.title = updatedTitle
        db.session.commit()
        return jsonify({'topic': topic_id})
    else:
        return jsonify({'error': 'Dữ liệu không hợp lệ'}), 400

@app.route('/delete_topic', methods=['POST'])
def delete_topic():
    data = request.get_json()
    if 'topic_id' in data:
        topic_id = data['topic_id']
        db.session.query(Topic).filter_by(id=topic_id).delete()
        db.session.commit()
    else:
        return jsonify({'error': 'Dữ liệu không hợp lệ'}), 400

@app.route('/add_conversation', methods=['POST'])
def add_conversation():
    data = request.get_json()
    if 'topic_id' in data:
        topic_id = data['topic_id']
        user_chat = data['user_chat']
        bot_chat = get_conversation_chain(vec)({"question": (prompt + user_chat)})
        conversation = Conversation( user_chat = user_chat, bot_chat = bot_chat["answer"], topic_id = topic_id)
        db.session.add(conversation)
        db.session.commit()
        return jsonify({'user_chat': user_chat, 'bot_chat': bot_chat["answer"]})
    else:
        user_chat = data['user_chat']
        bot_chat = get_conversation_chain(vec)({"question": (prompt + user_chat)})
        return jsonify({'user_chat': user_chat, 'bot_chat': bot_chat["answer"]})
