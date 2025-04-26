from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, ValidationError

app = Flask(__name__)
app.secret_key='njifnvdfsdcdcrvsdccdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)

#DB models
class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    number=db.Column(db.String(10))

    def __repr__(self):
        return f"User({self.username},{self.email},{self.id})"
    
#FORMS
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



@app.route("/")
def home():
    return render_template('home.html',title='TheNewsGround')

@app.route("/thehindu")
def thehindu():
    return render_template('TheHindu.html', title='TheHindu')

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data,number=form.mob_num.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!",'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and form.password.data==user.password:
            
            flash(f"{form.username.data} Logged in!",'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__=="__main__":
    app.run(debug=True)