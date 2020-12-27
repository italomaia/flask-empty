{%- set uses_socketio = cookiecutter.use_socketio in ('yes', 'y') -%}

from main import app_factory
from config import project_name
import os

try:
    config_obj_path = os.environ['FLASK_CONFIG_DEFAULT']
except KeyError:
    print(
        "Please, provide the environment variable FLASK_CONFIG_DEFAULT. "
        "It tells the application which configuration class to load.")
    exit()

app = app_factory(config_obj_path, project_name)


if __name__ == '__main__':
    _debug = app.config.get('DEBUG', False)

    kwargs = {
        'host': os.getenv('FLASK_HOST', '0.0.0.0'),
        'port': int(os.getenv('FLASK_PORT', 5000)),
        'debug': _debug,
        'use_reloader': app.config.get('USE_RELOADER', _debug),
        **app.config.get('SERVER_OPTIONS', {})
    }

    {% if uses_socketio -%}
    from extensions import io

    io.run(app, **kwargs)
    {% else %}
    app.run(**kwargs)
    {% endif %}
