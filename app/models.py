from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import current_user
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
   

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    def updateUserInfo(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

class FivePokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke1_name=db.Column(db.String(50))
    poke2_name=db.Column(db.String(50))
    poke3_name=db.Column(db.String(50))
    poke4_name=db.Column(db.String(50))
    poke5_name=db.Column(db.String(50))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, poke1_name, poke2_name, poke3_name, poke4_name, poke5_name, user_id):
            self.poke1_name=poke1_name
            self.poke2_name=poke2_name
            self.poke3_name=poke3_name
            self.poke4_name=poke4_name
            self.poke5_name=poke5_name
            self.user_id = user_id
          