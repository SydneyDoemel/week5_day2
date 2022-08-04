from flask_login import UserMixin
import requests
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
    def grab(self, poke):
        self.caught_pokes.append(poke)
        db.session.commit()

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
          

class Pokes(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
   

    def __init__(self, name):
        self.name = name
        
    def get_poke_func(self,name):
        
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)

        data = response.json()
        get_data = []
        poke_dict = {}
        poke_name = data['forms'][0]['name']
        poke_dict[poke_name] = {
            'Name' : data['forms'][0]['name'],
            'Ability' : data['abilities'][0]['ability']['name'],
            'Base Experience' : data['base_experience'],
            'front_shiny URL' : data['sprites']['front_shiny'],
            'attack base_stat' : data['stats'][1]['base_stat'],
            'hp base_stat' : data['stats'][0]['base_stat'],
            'defense base_stat': data['stats'][2]['base_stat']
            }
            
        get_data.append(poke_dict)
        return get_data

class CaughtPokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    poke_id=db.Column(db.Integer, db.ForeignKey('pokes.id'))

    def __init__(self, user_id, poke_id):
            self.poke_id= poke_id
            self.user_id = user_id