try:
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension()
except ImportError:
    print('debugtoolbar extension not available.')


{%- if cookiecutter.use_sql == 'yes' %}
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

{% endif %}


{%- if cookiecutter.use_nosql == 'yes' %}
from flask.ext.mongoengine import MongoEngine
nosql = MongoEngine()

{% endif %}

{%- if cookiecutter.use_socketio == 'yes' %}
from flask_socketio import SocketIO
socketio = SocketIO()

{% endif %}
