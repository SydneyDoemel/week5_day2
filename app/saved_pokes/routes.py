import requests
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required, user_loaded_from_request, user_logged_in
from .forms import SavePokeInfo
from app.models import FivePokes
saved_pokes = Blueprint('saved_pokes', __name__, template_folder='saved_pokestemplates')

from app.models import db



from app.search.get_poke_func import get_poke_func



@saved_pokes.route('/saved_pokes', methods=['GET', 'POST'])
def savePoke():
    form = SavePokeInfo()
    user_ids=FivePokes.query.all()
    userlst = []
    plst=[]
    try:
        for each in user_ids:
            userlst.append(each.user_id)
        if current_user.id in userlst:
            pokeslst = []
            mypokes = FivePokes.query.filter_by(user_id=current_user.id).first()
            pokeslst.append(mypokes.poke1_name)
            pokeslst.append(mypokes.poke2_name)
            pokeslst.append(mypokes.poke3_name)
            pokeslst.append(mypokes.poke4_name)
            pokeslst.append(mypokes.poke5_name)
            plst=[]
            for each in pokeslst:
                z = get_poke_func(each)
                x = z[0][each]
                plst.append(x)
                
            print(plst)
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
                return redirect(url_for('saved_pokes.savePoke'))
            else:
                print('validation failed')
        else:
            print('get request made')
    except:
        return redirect(url_for('saved_pokes.savePoke'))
 
    return render_template('saved_pokes.html', form = form, userlst = userlst, plst = plst)

@saved_pokes.route('/update_pokes', methods=['GET', 'POST'])
def updatePoke():
    form = SavePokeInfo()
    new_pokes = FivePokes.query.filter_by(user_id=current_user.id).first()
    
    if current_user.id != new_pokes.user_id:
        return redirect(url_for('saved_pokes.savePoke'))
    try:
        if request.method == "POST":
            if form.validate():
                poke1_name = form.poke1_name.data
                poke2_name = form.poke2_name.data
                poke3_name = form.poke3_name.data
                poke4_name = form.poke4_name.data
                poke5_name = form.poke5_name.data
                new_pokes.poke1_name = poke1_name
                new_pokes.poke2_name = poke2_name
                new_pokes.poke3_name = poke3_name
                new_pokes.poke4_name = poke4_name
                new_pokes.poke5_name = poke5_name
                db.session.commit()
                return redirect(url_for('profile.goToProfile'))
    except:
         return redirect(url_for('saved_pokes.savePoke'))
 

    return render_template('update_pokes.html', form=form, new_pokes = new_pokes)