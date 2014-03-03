# coding:utf-8

from database import db


class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    creation_datetime = db.Column(db.DateTime)
    brand = db.Column(db.String(100))
    website = db.Column(db.String(100))


class SKU(db.Model):
    __tablename__ = 'sku'

    id = db.Column(db.Integer, primary_key=True)
    creation_datetime = db.Column(db.DateTime)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    brand = db.relationship('Brand', backref=db.backref('sku_set', lazy='dynamic'))

    model = db.Column(db.String(100))
    teaser = db.Column(db.String(100))
    details = db.Column(db.Text)
    technical_details = db.Column(db.Text)
    mean_score = db.Column(db.SmallInteger)
    #comments


# TODO: this probably should move to another app
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    creation_datetime = db.Column(db.DateTime)

    sku_id = db.Column(db.Integer, db.ForeignKey('sku.id'))
    sku = db.relationship('SKU', backref=db.backref('comments', lazy='dynamic'))

    score = db.Column(db.SmallInteger)
    comment = db.Column(db.Text)