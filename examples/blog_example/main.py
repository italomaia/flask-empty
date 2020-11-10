# coding:utf-8

import os
import sys
from empty import Empty
from mixins import HttpMixin

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# allows you to copy json snippets directly into python
__builtin__.true = True
__builtin__.false = False
__builtin__.null = None


# define base classes for our App class
base_cls_list = [Empty]
base_cls_list = [HttpMixin] + base_cls_list


# apps is a special folder where you can place your blueprints
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))

basestring = getattr(__builtins__, 'basestring', str)


# dynamically create our class
App = type('App', tuple(base_cls_list), {})


def config_str_to_obj(cfg):
    if isinstance(cfg, basestring):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(config, app_name, blueprints=None):
    from commands import new_app, test_cmd

    # you can use Empty directly if you wish
    app = App(app_name, template_folder=os.path.join(PROJECT_PATH, 'templates'))
    config = config_str_to_obj(config)

    app.cli.add_command(new_app)
    app.cli.add_command(test_cmd)

    app.configure(config)
    app.add_blueprint_list(blueprints or config.BLUEPRINTS)
    app.setup()

    return app


def heroku():
    from config import Config, project_name
    # setup app through APP_CONFIG envvar
    return app_factory(Config, project_name)
