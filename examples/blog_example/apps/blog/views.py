# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from extensions import db

from .forms import PostForm
from .models import Post

app = Blueprint('blog', __name__, template_folder='templates')


@app.route("/")
def list_posts_view():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route("/add/", methods=['get', 'post'])
def add_post_view():
    form = PostForm()

    if form.validate_on_submit():
        try:
            obj = Post(
                form.title.data,
                form.text.data)
            db.session.add(obj)
            db.session.commit()
            flash('Post add successfully')
            return redirect(url_for('blog.list_posts_view'))
        except IntegrityError:
            flash('There is already a post with that title. Please, try another.')

    return render_template('blog/add_post.html', form=form)


@app.route("/<slug>/")
def post_view(slug):
    post = Post.query.filter_by(slug=slug).first()
    return render_template('blog/post.html', post=post)