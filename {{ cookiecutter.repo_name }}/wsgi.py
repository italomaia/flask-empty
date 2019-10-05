# coding:utf-8

from main import app_factory
from config import project_name
import os

try:
    config_obj_path = os.environ['FLASK_CONFIG_DEFAULT']
except KeyError as e:
    print("Please, provide the environment variable FLASK_CONFIG_DEFAULT. It is required.")
    exit()

app = app_factory(config_obj_path, project_name)


if __name__ == '__main__':
    args = (app,)
    kwargs = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug': os.getenv('FLASK_DEBUG', '0') == '1',
        'use_reloader': os.getenv('FLASK_DEBUG', '0') == '1',
    }

    {% if cookiecutter.use_socketio -%}
    from extensions import io
    io.run(*args, **kwargs)
    {% else %}
    app.run(*args, **kwargs)
    {% endif %}
