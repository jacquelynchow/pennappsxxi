from flask import Flask, render_template, url_for, request, redirect
from app import app
from datetime import date

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    today = date.today()
    # if user submitted an entry, get it from the form and re-route to the entry page
    if request.method == 'POST':
        entry_details = request.form.get('entry')
        entry_title = request.form.get('entry-title')
        return redirect(url_for('entry'))
    return render_template('index.html', date=today)

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
        return redirect(url_for('saveData', entry_details=entry_details))
    return render_template("recordVoice.html")

@app.route("/save")
def saveData():
    entry_title = request.args.get('entry_title')
    entry_details = request.args.get('entry_details')
    return render_template('save.html', entry_details=entry_details, entry_title=entry_title)

@app.route('/entries', methods=["GET", "POST"])
def entries():
    # if user submitted an entry, get it from the form and re-route to the entry page
    if request.method == 'POST':
        return redirect(url_for('entry'))
    return render_template('entries.html')

@app.route('/entry', methods=["GET", "POST"])
def entry():
    title = "Just Hackathon Things"
    date = "2020-09-13"
    entry_details = "Dear diary today I had a great time hacking with my team at a hackathon"
    return render_template('singleEntry.html', title=title, date=date, entry_details=entry_details)