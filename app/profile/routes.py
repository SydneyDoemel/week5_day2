from flask import Blueprint, render_template, url_for, request, redirect, session
from flask_login import current_user
from app.auth.forms import UserUpdateForm
profile = Blueprint('profile', __name__, template_folder='profiletemplates')
from app.models import FivePokes, User
from app.models import db



from app.search.get_poke_func import get_poke_func

@profile.route('/profile', methods = ['GET', 'POST'])
def goToProfile():
    newlist = []
    try:
        poke1 = FivePokes.query.filter_by(user_id = current_user.id).first()
        poke1 = poke1.poke1_name
        z = get_poke_func(poke1)
        x1 = z[0][poke1]
        newlist.append(x1)
    except:
        pass
    try:
        poke2 = FivePokes.query.filter_by(user_id = current_user.id).first()
        poke2 = poke2.poke2_name
        z = get_poke_func(poke2)
        x2 = z[0][poke2]
        newlist.append(x2)
    except:
        pass
    try:
        poke3 = FivePokes.query.filter_by(user_id = current_user.id).first()
        poke3 = poke3.poke3_name
        z = get_poke_func(poke3)
        x3 = z[0][poke3]
        newlist.append(x3)
    except:
        pass
    try:
        poke4 = FivePokes.query.filter_by(user_id = current_user.id).first()
        poke4 = poke4.poke4_name
        z = get_poke_func(poke4)
        x4 = z[0][poke4]
        newlist.append(x4)
    except:
        pass
    try:
        poke5 = FivePokes.query.filter_by(user_id = current_user.id).first()
        poke5 = poke5.poke5_name
        z = get_poke_func(poke5)
        x5 = z[0][poke5]
        newlist.append(x5)
    except:
        pass
    
    

        
    form = UserUpdateForm()
    user = User.query.filter_by(id = current_user.id).first()
    if request.method =='POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            if username != "":
                user.username = username
            if email != "":
                user.email = email
            if password != "":
                user.password = password
            
            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.logMeIn'))
            except:
                pass
        else:
            print('validation failed')
    return render_template('profile.html', form = form, newlist = newlist)

