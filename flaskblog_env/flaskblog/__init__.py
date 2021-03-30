from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '08411f065bb1bc731052710b052ab510'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
from flaskblog import routes
from flaskblog.forms import RegistrationForm, LoginForm # folder_name.file_name -> flask_blog.forms
