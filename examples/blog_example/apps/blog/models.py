# -*- coding:utf-8 -*-
from extensions import db
from datetime import datetime
from flask import url_for


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    slug = db.Column(db.String(120), unique=True)
    text = db.Column(db.Text)

    def __init__(self, title, text, pub_date=None, slug=None):
        self.title = title
        self.text = text
        self.slug = (slug or title).replace(' ', '_')
        self.pub_date = (pub_date or datetime.utcnow())

    def __repr__(self):
        return self.title

    def absolute_url(self):
        return url_for('blog.post_view', slug=self.slug)