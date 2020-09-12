from flask import Flask, render_template, url_for, request, redirect
from app import app
from datetime import date

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    today = date.today()
    return render_template('index.html', title='Home', date=today)

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route('/record', methods=["GET", "POST"])
def record():
    # if user submitted an entry, get it from the form and re-route to the entry page
    if request.method == 'POST':
        entry_details = request.form.get('entry')
        return redirect(url_for('saveData', entry_details=entry_details))
    return render_template("recordVoice.html")

@app.route("/save")
def saveData():
    entry_details = request.args.get('entry_details')
    return render_template('save.html', entry_details=entry_details)

@app.route('/entries')
def entries():
    return render_template('entries.html')
