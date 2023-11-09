from datetime import datetime, timedelta
from chatPDF import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    topics = db.relationship('Topic', backref='userdetail', lazy=True)
    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}', '{self.password}')"

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, default='New chat')
    date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    conversations = db.relationship('Conversation', backref='topicdetail', lazy=True)
    def __repr__(self):
        return f"Topic('{self.id}', '{self.title}', '{self.date}')"

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_chat = db.Column(db.String(10000), nullable=False)
    bot_chat = db.Column(db.String(10000), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    def __repr__(self):
        return f"Conversation('{self.id}', '{self.user_chat}', '{self.bot_chat}')"