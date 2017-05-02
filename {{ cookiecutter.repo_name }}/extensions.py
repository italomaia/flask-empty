try:
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension()
except ImportError:
    print('debugtoolbar extension not available.')


{%- if cookiecutter.use_sql == 'yes' %}
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db=db)
{% endif %}

{%- if cookiecutter.use_admin %}
from flask_admin import Admin

admin = Admin()
{% endif %}


{%- if cookiecutter.use_nosql == 'yes' %}
from flask.ext.mongoengine import MongoEngine
nosql = MongoEngine()
{% endif %}

{%- if cookiecutter.rest_app == 'yes' %}
from flask_marshmallow import Marshmallow

ma = Marshmallow()

from flask_jsglue import JSGlue
glue = JSGlue()

from flask_limiter import Limiter
limiter = Limiter()
{% endif -%}

{%- if cookiecutter.use_async_tasks == 'yes' %}
from flask_socketio import SocketIO
io = SocketIO()

{% endif %}
