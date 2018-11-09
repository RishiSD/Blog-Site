import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, request, render_template, redirect, url_for, abort
)
from flask_login import (
    login_required, current_user, logout_user, login_user
)

from FlaskBlogApp.user import User, UserForm

user = Blueprint('user', __name__)


@user.route('/signup', methods=['GET', 'POST'])
def signup():
    if not os.environ.get('SIGNUP_ENABLED', True):
        abort(401)
    form = UserForm(request.form)
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if User.get_user_by_username(username=request.form['username']):
            return render_template('login.html', form=form,
                                   error="A user with username already exists")
        else:
            user = User(username=request.form['username'],
                        password=generate_password_hash(request.form['password']),
                        authenticated=False)
            user.save()
            return redirect(url_for('user.login'))


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        user = User.get_user_by_username(username=request.form['username'])
        if user and check_password_hash(user.password, request.form['password']):
            user.authenticated = True
            user.save()
            login_user(user, remember=True)
            return redirect(url_for('navigation.index_logged',
                                    username=user.username))
        else:
            return render_template('login.html', form=form,
                                   error="Invalid Credentials")


@user.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    user.save()
    logout_user()
    return redirect(url_for('navigation.index'))
