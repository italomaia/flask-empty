# coding:utf-8

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class PostForm(Form):
    title = TextField('title', validators=[DataRequired()])
    slug = TextField('slug')
    text = TextField('content', validators=[DataRequired()])
