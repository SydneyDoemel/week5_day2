from flask import Blueprint, render_template, request, redirect
from app.models import User
saved_pokes = Blueprint('saved_pokes', __name__, template_folder='saved_pokestemplates')
from app.models import db

@saved_pokes.route('/saved_pokes', methods=['GET', 'POST'])
def seeMyPokes():
    if request.method =='POST':
        print('request made')
    return render_template('saved_pokes.html')
