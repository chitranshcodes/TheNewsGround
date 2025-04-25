from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='njifnvdfsdcdcrvsdccdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(20), nullable=False, unique=True)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    number=db.Column(db.String(10))

    def __repr__(self):
        return f"User({self.username},{self.email},{self.id})"

app.app_context().push()
db.drop_all()