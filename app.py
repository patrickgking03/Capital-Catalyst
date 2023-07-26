from flask import Flask, render_template
from models import db, User, Transaction, Investment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/investments')
def investments():
    return render_template('investments.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
