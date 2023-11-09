from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8d995ee2e1b43236aaea002c'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push() 
from chatPDF import routes
from chatPDF.models import User, Topic, Conversation