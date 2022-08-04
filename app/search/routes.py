import requests
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from .forms import FindPokeInfo
from app.models import Pokes, CaughtPokes
from app.search.get_poke_func import get_poke_func
from app.models import db
search = Blueprint('search', __name__, template_folder='searchtemplates')

@search.route('/search', methods=["GET", "POST"])
def searchPokes():
    form = FindPokeInfo()
   
    if request.method == "POST":
        try:
            if form.validate():
                poke_you_want = form.pokefind.data
                z = get_poke_func(poke_you_want)
                x = z[0][poke_you_want]
                caught = []
                try:
                    new_poke = Pokes(poke_you_want)
                    print(new_poke)
                    db.session.add(new_poke)
                    db.session.commit()
                except:
                    new_poke = Pokes.query.filter_by(name = poke_you_want).first()
                    print(new_poke)
                if current_user.is_authenticated:
                    print('authenticated')
                    id = new_poke.id
                    caught = CaughtPokes.query.all()
                    print(caught)
                    for p in caught:
                        if p.poke_id == new_poke.id: #problem happening here
                            print('yes')
                            p.flag = True
                        else:
                            print('no')
                            p.flag = False
                    print(caught)
                
            return render_template('search.html',form = form, x = x, caught = caught )
                
        except:
            return redirect(url_for('search.searchPokes'))
        
    else:
        print('get request made')
    
    return render_template('search.html', form = form)

@search.route('/catch/<int:new_poke>', methods = ["GET", "POST"])
def catchPoke(new_poke):
    poke_id = new_poke.id
    user_id = current_user.id

    caught = CaughtPokes(poke_id, user_id)
    try:
        db.session.add(caught)
        db.session.commit()
        return redirect(url_for('search.searchPokes'))
    except:
        pass
        return redirect(url_for('search.searchPokes'))

