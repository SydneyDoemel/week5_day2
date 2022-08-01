from app import app
from flask import render_template
from flask_login import current_user
from app.models import FivePokes, User
from app.models import db
from app.search.get_poke_func import get_poke_func
@app.route('/')
def index():
    users = FivePokes.query.all()
    scores_dict = {}
    for each in users:
        # for num in len(range(6)):
        x = each.poke1_name
        z = get_poke_func(x)
        total_score1 = z[0][x]['Base Experience'] + z[0][x]['attack base_stat'] + z[0][x]['hp base_stat'] + z[0][x]['defense base_stat']
        x = each.poke2_name
        z = get_poke_func(x)
        total_score2 = z[0][x]['Base Experience'] + z[0][x]['attack base_stat'] + z[0][x]['hp base_stat'] + z[0][x]['defense base_stat']
        x = each.poke3_name
        z = get_poke_func(x)
        total_score3 = z[0][x]['Base Experience'] + z[0][x]['attack base_stat'] + z[0][x]['hp base_stat'] + z[0][x]['defense base_stat']
        x = each.poke4_name
        z = get_poke_func(x)
        total_score4 = z[0][x]['Base Experience'] + z[0][x]['attack base_stat'] + z[0][x]['hp base_stat'] + z[0][x]['defense base_stat']
        x = each.poke5_name
        z = get_poke_func(x)
        total_score5 = z[0][x]['Base Experience'] + z[0][x]['attack base_stat'] + z[0][x]['hp base_stat'] + z[0][x]['defense base_stat']
        overall = total_score1 + total_score2 + total_score3 + total_score4 + total_score5
        id = each.user_id
        username = User.query.get(id)
        
        scores_dict[overall] = username.username
    scores = sorted(scores_dict, reverse=True)
    
    return render_template('index.html', scores_dict=scores_dict, scores=scores)
