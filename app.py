from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.secret_key='njifnvdfsdcdcrvsdccdc'


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