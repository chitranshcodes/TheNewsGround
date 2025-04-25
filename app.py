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
db.create_all()

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
        flash(f"{form.username.data} Logged in!",'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__=="__main__":
    app.run(debug=True)