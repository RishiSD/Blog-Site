import datetime

from flask import render_template, request, Blueprint, redirect, url_for, abort
from flask_login import login_required, current_user
from FlaskBlogApp.posts import Posts, PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/<string:post_id>')
def post(post_id):
    post = Posts.objects.get(id=post_id)
    return render_template('post.html', post=post)


@posts.route('/userpost/<string:username>')
@login_required
def user_post(username):
    posts = Posts.objects(author=username).all().order_by('-date_posted')
    return render_template('my_posts.html', posts=posts, username=username)


@posts.route('/add', methods=['GET', 'POST'])
@login_required
def addpost():
    if request.method == 'GET':
        form = PostForm(request.form)
        return render_template('add.html', form=form)
    else:
        post = Posts(title=request.form['title'],
                     subtitle=request.form['subtitle'],
                     author=current_user.username,
                     content=request.form['content'],
                     date_posted=datetime.datetime.now())
        post.save()

        return redirect(url_for('posts.post', post_id=post.pk))


@posts.route('/edit/<string:post_id>', methods=['GET', 'POST'])
@login_required
def editpost(post_id):
    post = Posts.objects.get(id=post_id)
    if request.method == 'GET':
        if current_user.username != post.author:
            abort(401)
        form = PostForm(request.form)
        return render_template('add.html', form=form, post=post)
    else:
        Posts.objects(id=post.id).update(title=request.form['title'],
                                         subtitle=request.form['subtitle'],
                                         author=current_user.username,
                                         content=request.form['content'],
                                         date_posted=datetime.datetime.now())
        post.reload()

        return redirect(url_for('posts.post', post_id=post.pk))


@posts.route('/delete/<string:post_id>')
@login_required
def deletepost(post_id):
    post = Posts.objects.get(id=post_id)
    if current_user.username != post.author:
        abort(401)
    post.delete()
    return redirect(url_for('posts.user_post', username=current_user.username))
