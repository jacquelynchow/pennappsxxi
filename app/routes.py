from flask import Flask, render_template, url_for
from app import app

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    user = {'username': 'Alice'}
    return render_template('index.html', title='Home', user=user)
