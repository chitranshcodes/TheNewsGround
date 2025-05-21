from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, ValidationError

#password
from flask_bcrypt import Bcrypt
#login
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

#bs4 scripts
from scripts import thehinduinternational, thehindunational, thehindubreaking, thehindueconomy, toidelhi, toiup, toibusiness, toisports,tet

app = Flask(__name__)
app.secret_key='RQb4gEeXNxMJ0KHE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
LM=LoginManager(app)

#DB models
@LM.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    number=db.Column(db.String(10))
    notes=db.relationship('Note', backref='author')

    def __repr__(self):
        return f"User({self.username},{self.email},{self.id})"
class Note(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    content=db.Column(db.Text(), nullable=False)
    user_id=db.Column(db.Integer(), db.ForeignKey('user.id'))

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

class NoteForm(FlaskForm):
    content=StringField('content',validators=[DataRequired()])
    submit=SubmitField('Add Note')

#db
app.app_context().push()
db.create_all()

@app.route("/")
def home():
    return render_template('home.html',title='TheNewsGround')

@app.route("/thehindu")
def thehindu():
    element1=thehinduinternational()
    element2=thehindunational()
    element3=thehindubreaking()
    element4=thehindueconomy()
    return render_template('TheHindu.html', title='TheHindu', element1=element1, element2=element2, element3=element3, element4=element4)

@app.route("/thetoi")
def thetoi():
    element1=toidelhi()
    element2=toiup()
    element3=toibusiness()
    element4=toisports()
    return render_template('thetoi.html', title='TheTimesOfIndia', element1=element1, element2=element2, element3=element3, element4=element4)

@app.route('/theet')
def theet():
    element=tet()
    return render_template('tet.html', title='TheEconomicTimes', element=element)

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw,number=form.mob_num.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!",'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='register')

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"{form.username.data} LogIn successful",'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form, title='login')

@app.route('/addnote', methods=['POST','GET'])
@login_required
def addnote():
    form=NoteForm()
    if form.validate_on_submit():
        note=Note(content=form.content.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash(f"Hurray!! Posted a new note")
        return redirect(url_for('home'))
    return render_template('addnote.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/notes')
@login_required
def notes():
    posts=Note.query.filter_by(user_id=current_user.id).all()
    return render_template('notes.html', posts=posts)

if __name__=="__main__":
    app.run(debug=True)