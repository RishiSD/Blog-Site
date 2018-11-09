from flask import render_template, Blueprint
from flask_login import login_required, current_user
from FlaskBlogApp.posts import Posts

navigation = Blueprint('navigation', __name__)


@navigation.route('/')
def index():
    posts = Posts.objects().all().order_by('-date_posted')
    return render_template('index.html', posts=posts)


@navigation.route('/<string:username>')
@login_required
def index_logged(username):
    posts = Posts.objects().all().order_by('-date_posted')
    return render_template('index.html', posts=posts,
                           username=username)


@navigation.route('/about')
def about():
    return render_template('about.html')


@navigation.route('/contact')
def contact():
    return render_template('contact.html')
