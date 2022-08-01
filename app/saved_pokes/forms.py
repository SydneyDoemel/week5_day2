from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired

class SavePokeInfo(FlaskForm):
   
    poke1_name = StringField('Poke1_name')
    poke2_name = StringField('Poke2_name')
    poke3_name =StringField('Poke3_name')
    poke4_name =StringField('Poke4_name')
    poke5_name =StringField('Poke5_name')
   #maybe add EqualTo to pokefind.. how to make sure the poke name is in the poke API?
  
    save= SubmitField()
   
    #save poke here?
