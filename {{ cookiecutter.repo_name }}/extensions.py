{%- set uses_cockroachdb = cookiecutter.use_sql_cockroachdb in ('y', 'yes') -%}
{%- set uses_postgres = cookiecutter.use_sql_postgres in ('y', 'yes') -%}
{%- set uses_mysql = cookiecutter.use_sql_mysql in ('y', 'yes') -%}
{%- set uses_sql = uses_cockroachdb or uses_postgres or uses_mysql -%}
{%- set uses_mongodb = cookiecutter.use_nosql_mongodb in ('y', 'yes') -%}
{%- set uses_socketio = cookiecutter.use_socketio in ('yes', 'y') -%}

import os
{% if uses_sql %}
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
{%- endif -%}
{%- if cookiecutter.use_security in ('yes', 'y') %}
from flask_security import Security
{%- endif -%}
{%- if cookiecutter.use_admin in ('yes', 'y') %}
from flask_admin import Admin
{%- endif -%}
{%- if uses_mongodb %}
from flask_mongoengine import MongoEngine
{%- endif -%}
{%- if cookiecutter.use_rest in ('yes', 'y') %}
from flask_marshmallow import Marshmallow
from flask_jsglue import JSGlue
{%- endif -%}
{%- if uses_socketio %}
from flask_socketio import SocketIO
{%- endif %}
{%- if cookiecutter.use_async_tasks in ('yes', 'y') %}
from flask_rq2 import RQ
{% endif %}

toolbar = None

if os.environ['FLASK_CONFIG_DEFAULT'] == 'Dev':
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension()

{% if uses_sql %}
db = SQLAlchemy()
migrate = Migrate(db=db)
{% endif -%}
{%- if cookiecutter.use_admin in ('yes', 'y') -%}
admin = Admin()
{% endif -%}
{%- if uses_mongodb -%}
nosql = MongoEngine()
{% endif -%}
{%- if cookiecutter.use_rest in ('yes', 'y') -%}
ma = Marshmallow()
glue = JSGlue()
{% endif -%}
{%- if cookiecutter.use_async_tasks in ('yes', 'y') -%}
io = SocketIO()
{% endif -%}
{%- if cookiecutter.use_async_tasks in ('yes', 'y') -%}
rq = RQ()
{% endif -%}
{% if cookiecutter.use_security in ('yes', 'y') -%}
security = Security()


def security_init_kwargs():
    """
    **kwargs arguments passed down during security extension initialization by
    "empty" package.
    """
    return dict()
{% endif -%}
