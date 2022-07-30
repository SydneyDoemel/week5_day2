from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired

class FindPokeInfo(FlaskForm):
    pokefind = StringField(validators=[InputRequired()])
    #maybe add EqualTo to pokefind.. how to make sure the poke name is in the poke API?
    search = SubmitField()
    
    #save poke here?
