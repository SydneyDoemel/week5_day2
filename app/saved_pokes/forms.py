from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired

class SavePokeInfo(FlaskForm):
   
    poke1_name = StringField('Poke1_name', validators=[InputRequired()])
    poke2_name =StringField('Poke2_name', validators=[InputRequired()])
    poke3_name =StringField('Poke3_name', validators=[InputRequired()])
    poke4_name =StringField('Poke4_name', validators=[InputRequired()])
    poke5_name =StringField('Poke5_name', validators=[InputRequired()])

   #maybe add EqualTo to pokefind.. how to make sure the poke name is in the poke API?
  
    save = SubmitField()
    #save poke here?
