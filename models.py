from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(120))
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset = db.Column(db.String(120))
    quantity = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
