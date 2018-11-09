from flask import render_template, abort
from FlaskBlogApp import login_manager
from FlaskBlogApp.user import User


def unauthorized_access(e):
    return render_template('error.html', error='401',
                           err_text='Unauthorized Access'), 401


def page_not_found(e):
    return render_template('error.html', error='404',
                           err_text='Oops! Page not found'), 404


@login_manager.user_loader
def user_loader(username):
    return User.objects.get(username=username)
