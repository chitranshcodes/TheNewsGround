from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('layout.html',title='TheNewsGround')

@app.route("/thehindu")
def thehindu():
    return render_template('TheHindu.html', title='TheHindu')

if __name__=="__main__":
    app.run(debug=True)