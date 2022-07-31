from flask import Blueprint, render_template
profile = Blueprint('profile', __name__, template_folder='profiletemplates')
from app.models import FivePokes
from app.models import db



from app.search.get_poke_func import get_poke_func

@profile.route('/profile')
def goToProfile():
    poke1 = FivePokes.query.filter_by(user_id = 1).first()
    poke1 = poke1.poke1_name
    z = get_poke_func(poke1)
    x1 = z[0][poke1]

    poke2 = FivePokes.query.filter_by(user_id = 1).first()
    poke2 = poke2.poke2_name
    z = get_poke_func(poke2)
    x2 = z[0][poke2]

    poke3 = FivePokes.query.filter_by(user_id = 1).first()
    poke3 = poke3.poke3_name
    z = get_poke_func(poke3)
    x3 = z[0][poke3]

    poke4 = FivePokes.query.filter_by(user_id = 1).first()
    poke4 = poke4.poke4_name
    z = get_poke_func(poke4)
    x4 = z[0][poke4]

    poke5 = FivePokes.query.filter_by(user_id = 1).first()
    poke5 = poke5.poke5_name
    z = get_poke_func(poke5)
    x5 = z[0][poke5]
    newlist = []
    newlist.append(x1)
    newlist.append(x2)
    newlist.append(x3)
    newlist.append(x4)
    newlist.append(x5)
    return render_template('profile.html', newlist=newlist)