try:
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension()
except ImportError:
    print('debugtoolbar extension not available.')

{% if cookiecutter.use_sql == 'yes' %}
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
{%- endif -%}

{%- if cookiecutter.use_security == 'yes' %}
from flask_security import Security
{%- endif -%}

{%- if cookiecutter.use_admin %}
from flask_admin import Admin
{%- endif -%}

{%- if cookiecutter.use_nosql == 'yes' %}
from flask_mongoengine import MongoEngine
{%- endif -%}

{%- if cookiecutter.rest_app == 'yes' %}
from flask_marshmallow import Marshmallow
from flask_jsglue import JSGlue
{%- endif -%}

{%- if cookiecutter.use_async_tasks == 'yes' %}
from flask_socketio import SocketIO
{%- endif %}

{%- if cookiecutter.use_async_tasks == 'yes' %}
from flask_rq2 import RQ
{% endif %}


{%- if cookiecutter.use_sql == 'yes' %}
db = SQLAlchemy()
migrate = Migrate(db=db)
{% endif -%}

{%- if cookiecutter.use_admin %}
admin = Admin()
{% endif -%}

{%- if cookiecutter.use_nosql == 'yes' %}
nosql = MongoEngine()
{% endif -%}

{%- if cookiecutter.rest_app == 'yes' %}
ma = Marshmallow()
glue = JSGlue()
{% endif -%}

{%- if cookiecutter.use_async_tasks == 'yes' %}
io = SocketIO()
{% endif -%}

{%- if cookiecutter.use_async_tasks == 'yes' %}
rq = RQ()
{% endif -%}

{% if cookiecutter.use_security == 'yes' %}
security = Security()


def security_extra():
    pass
{% endif -%}
