from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key='RQb4gEeXNxMJ0KHE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
LM=LoginManager(app)

from thenewsmania import routes