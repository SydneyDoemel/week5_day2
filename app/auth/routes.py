from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm
from .forms import UserLoginForm
from app.models import User
auth = Blueprint('auth', __name__, template_folder = 'authtemplates')
from app.models import db
@auth.route('/login')
def logMeIn():
    form = UserLoginForm()
    if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        return redirect(url_for('/index'))
    else:
        print('validation failed')
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