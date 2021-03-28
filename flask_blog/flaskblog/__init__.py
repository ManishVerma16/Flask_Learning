from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm # folder_name.file_name -> flask_blog.forms
# from models import User, Post

app = Flask(__name__)

app.config['SECRET_KEY'] = '08411f065bb1bc731052710b052ab510'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///mysql.db'


db = SQLAlchemy(app)

from flaskblog import routes