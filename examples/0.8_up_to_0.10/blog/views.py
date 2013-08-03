# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, request
from models import Post

app = Blueprint('blog', __name__, template_folder='templates')

@app.route("/")
def index_view():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route("/<post_slug>")
def post_view(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post)