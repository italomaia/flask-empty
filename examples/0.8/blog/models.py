# -*- coding:utf-8 -*-
from database import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    slug = db.Column(db.String(120))
    text = db.Column(db.Text)

    def __init__(self, title, text, pub_date=None, slug=None):
        self.title = title
        self.text = text
        self.slug = (slug or title).replace(' ', '_')
        self.pub_date = (pub_date or datetime.utcnow())

    def __repr__(self):
        return self.title
