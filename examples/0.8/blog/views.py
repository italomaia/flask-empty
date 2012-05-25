# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, request

app = Blueprint('blog', __name__, template_folder='templates')

@app.route("/")
def index_view():
    return render_template('blog/index.html')