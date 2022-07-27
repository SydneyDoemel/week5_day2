from flask import Blueprint, render_template
saved_pokes = Blueprint('saved_pokes', __name__, template_folder='saved_pokestemplates')

@saved_pokes.route('/saved_pokes')
def seeMyPokes():
    return render_template('saved_pokes.html')