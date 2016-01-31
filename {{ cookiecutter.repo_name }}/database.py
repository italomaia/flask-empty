# -*- coding:utf-8 -*-

{%- if cookiecutter.use_sql == 'yes' %}
#--- SQLALCHEMY SUPPORT

from extensions import db


def drop_all():
    db.drop_all()


def create_all():
    db.create_all()


def remove_session():
    db.session.remove()

#--- SQLALCHEMY SUPPORT END
{% endif %}

{%- if cookiecutter.use_nosql == 'yes' %}
from extensions import nosql

{% endif %}
