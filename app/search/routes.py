import requests
from flask import Blueprint, render_template, request
from .forms import FindPokeInfo

from app.search.get_poke_func import get_poke_func

search = Blueprint('search', __name__, template_folder='searchtemplates')

@search.route('/search', methods=["GET", "POST"])
def searchPokes():
    form = FindPokeInfo()
    if request.method == "POST":
        if form.validate():
            poke_you_want = form.pokefind.data
            z = get_poke_func(poke_you_want)
            x = z[0][poke_you_want]
            return render_template('search.html',form = form, x = x)
        else:
            print('validation failed')
    else:
        print('get request made')
 
    return render_template('search.html', form = form)

