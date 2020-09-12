from flask import Flask, render_template, url_for, request, redirect
from app import app

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    user = {'username': 'Alice'}
    return render_template('index.html', title='Home', user=user)

@app.route('/record', methods = ['GET', 'POST'])
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
