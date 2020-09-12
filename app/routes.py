from flask import Flask, render_template, url_for
from app import app

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    user = {'username': 'Alice'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')