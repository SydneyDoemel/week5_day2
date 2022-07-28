from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    poke1 = db.Column(db.String(200))
    poke2 = db.Column(db.String(200))
    poke3 = db.Column(db.String(200))
    poke4 = db.Column(db.String(200))
    poke5 = db.Column(db.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


