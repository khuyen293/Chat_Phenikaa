from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.storage.file_system import LocalFileStore
from langchain.embeddings.cache import CacheBackedEmbeddings

from selenium import webdriver
from bs4 import BeautifulSoup

from dotenv import load_dotenv
import os  
import pickle

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
    # return clean_text(text)
    return text

def get_web_text(url):
    text = ""
    driver = webdriver.Chrome()
    driver.get(url)
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')
    target_div = soup.find('div', {'class': "news-item-content"})
    if target_div is not None:
        elements = target_div.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul'])
        for element in elements:
            text += element.get_text() + "\n"
    else:
        print("Không tìm thấy nội dung.")
    return text

def get_webs_text(urls):
    all_texts = ""
    for url in urls:
        result = get_web_text(url)
        all_texts += result
    return all_texts


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
    fs = LocalFileStore("./cache/")
    underlying_embeddings = OpenAIEmbeddings()
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, fs, namespace=underlying_embeddings.model
    )
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding= cached_embedder)
    return vectorstore

prompt = """You are an AI assistant created by Phenikaa University to answer questions about the university and have friendly conversations with students. 
Your goal is to be helpful, exaclly. 
If you can't find the information, say you don't know. Don't try to make up answers.
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
    
def save_vectorstore(vectorstore, filename):
    with open(filename, 'wb') as file:
        pickle.dump(vectorstore, file)
        
def load_vectorstore(filename):
    with open(filename, 'rb') as file:
        vectorstore = pickle.load(file)
    return vectorstore

def get_data():
    text = get_pdfs_text(["../chatPDF/pdf/Thoi khoa bieu Tuan SHCD K15- Ngày 15.9.2021.pdf","../chatPDF/pdf/Thông báo về việc xin miễn giảm và nộp học phí .pdf", "../chatPDF/pdf/Tb_ra_vao_cong.pdf", "../chatPDF/pdf/ctdtict1-1.pdf"]) + get_webs_text(["https://phenikaa-uni.edu.vn/vi/events/view/su-kien/phenikaa-university-faculty-of-business-and-economics-conference-pubec-2023", "https://phenikaa-uni.edu.vn/vi/events/view/su-kien/hoi-nghi-nu-khoa-hoc-toan-quoc-lan-thu-iii"])
    chunks = get_text_chunks(text)
    vec = get_vectorstore(chunks)
    save_vectorstore(vec, './cache/vectorstore.pkl')

get_data()