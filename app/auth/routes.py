from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import UserCreationForm
from .forms import UserLoginForm
from flask_login import login_user, logout_user, login_required, current_user

from app.models import User
auth = Blueprint('auth', __name__, template_folder = 'authtemplates')
from app.models import db
@auth.route('/login', methods = ['GET', 'POST'])
def logMeIn():
    form = UserLoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(username = username).first()
            if user:
                if password == user.password:
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect password')
            else:
                pass
    return render_template('login.html', form=form)

@auth.route('/signup', methods = ['GET', 'POST'])
def signMeUp():
    form = UserCreationForm()
    if request.method =='POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.logMeIn'))
        else:
            print('validation failed')
    return render_template('signup.html', form = form)




@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('index'))