from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, ValidationError
from thenewsmania.models import User
from thenewsmania import bcrypt

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(), Length(min=6)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    mob_num=IntegerField('mobile number', validators=[Optional()])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='passwords must match')])
    submit=SubmitField('Sign-Up')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Use a different email')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Use a different username')  


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Log-In')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No username exists')
    def validate_password(self,password):
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            raise ValidationError("username doesn't exist")
        if not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('wrong password')
            

class NoteForm(FlaskForm):
    content=StringField('content',validators=[DataRequired()])
    submit=SubmitField('Add Note')