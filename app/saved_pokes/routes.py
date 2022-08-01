import requests
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, user_logged_in
from .forms import SavePokeInfo
from app.models import FivePokes
saved_pokes = Blueprint('saved_pokes', __name__, template_folder='saved_pokestemplates')

from app.models import db



from app.search.get_poke_func import get_poke_func



@saved_pokes.route('/saved_pokes', methods=['GET', 'POST'])
def savePoke():
    form = SavePokeInfo()
    if request.method == 'POST':
        if form.validate():
            poke_you_want = form.poke1_name.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            poke1_name = x['Name']

            poke_you_want = form.poke2_name.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            poke2_name = x['Name']

            poke_you_want = form.poke3_name.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            poke3_name = x['Name']

            poke_you_want = form.poke4_name.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            poke4_name = x['Name']

            poke_you_want = form.poke5_name.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            poke5_name = x['Name']
            new_poke = FivePokes(poke1_name, poke2_name, poke3_name, poke4_name, poke5_name, current_user.id)
            db.session.add(new_poke)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            print('validation failed')
    else:
        print('get request made')
 
    return render_template('saved_pokes.html', form = form)

