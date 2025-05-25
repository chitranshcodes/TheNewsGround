from flask import render_template, redirect, url_for, flash

#login
from flask_login import login_user, current_user, logout_user, login_required

#bs4 scripts
from thenewsmania.scripts import thehinduinternational, thehindunational, thehindubreaking, thehindueconomy, toidelhi, toiup, toibusiness, toisports,tet, newsapi
from thenewsmania import app,bcrypt,db
from thenewsmania.models import User, Note
from thenewsmania.forms import RegistrationForm, LoginForm, NoteForm

from apscheduler.schedulers.background import BackgroundScheduler
#caching
thehindu_cache={}
thetoi_cache={}
theet_cache={}
api_cache={}


def update_thehindu():
    thehindu_cache['element1']=thehinduinternational()
    thehindu_cache['element2']=thehindunational()
    thehindu_cache['element3']=thehindubreaking()
    thehindu_cache['element4']=thehindueconomy()

def update_thetoi():
    thetoi_cache['element1']=toidelhi()
    thetoi_cache['element2']=toiup()
    thetoi_cache['element3']=toibusiness()
    thetoi_cache['element4']=toisports()

def update_theet():
    theet_cache['element1']=tet()

def update_api():
    api_cache['element']=newsapi()

scheduler=BackgroundScheduler()
scheduler.add_job(update_thehindu, 'interval', minutes=15)
scheduler.add_job(update_thetoi, 'interval', minutes=15)
scheduler.add_job(update_theet, 'interval', minutes=15)
scheduler.add_job(update_api, 'interval', minutes=15)
scheduler.start()

update_thehindu()
update_thetoi()
update_theet()
update_api()

@app.route("/")
def home():
    return render_template('home.html',title='TheNewsGround')

@app.route("/thehindu")
def thehindu():
    return render_template('TheHindu.html', title='TheHindu', element1=thehindu_cache['element1'], element2=thehindu_cache['element2'], element3=thehindu_cache['element3'], element4=thehindu_cache['element4'])

@app.route("/thetoi")
def thetoi():
    return render_template('thetoi.html', title='TheTimesOfIndia',element1=thetoi_cache['element1'], element2=thetoi_cache['element2'], element3=thetoi_cache['element3'], element4=thetoi_cache['element4'])

@app.route('/theet')
def theet():
    return render_template('tet.html', title='TheEconomicTimes', element=theet_cache['element1'])

@app.route('/api')
def api():
    return render_template('api.html', title='Api-News', element=api_cache['element'])

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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')