# -*- coding:utf-8 -*-

{%- if cookiecutter.use_sql == 'yes' %}
#--- SQLALCHEMY SUPPORT

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def drop_all():
    db.drop_all()


def create_all():
    db.create_all()


def remove_session():
    db.session.remove()

#--- SQLALCHEMY SUPPORT END
{% endif %}