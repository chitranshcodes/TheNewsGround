from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, optional
class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(), Length(min=6)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    mob_num=IntegerField('mobile number', validators=[optional(), Length(min=10,max=10)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='passwords must match')])
    submit=SubmitField('Sign-Up')
class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Log-In')