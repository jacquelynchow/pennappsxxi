from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alice'}
    return render_template('index.html', title='Home', user=user)

@app.route('/record')
def record():
    return render_template('recordVoice.html')
