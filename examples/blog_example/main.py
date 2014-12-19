# -*- coding:utf-8 -*-

from empty import Empty

import sys
import os

# apps is a special folder where you can place your blueprints
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))

basestring = getattr(__builtins__, 'basestring', str)


class App(Empty):
    def configure_database(self):
        "Database configuration should be set here"
        # uncomment for sqlalchemy support
        from database import db
        db.app = self
        db.init_app(self)


def config_str_to_obj(cfg):
    if isinstance(cfg, basestring):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(config, app_name, blueprints=None):
    # you can use Empty directly if you wish
    app = App(app_name)
    config = config_str_to_obj(config)

    app.configure(config)
    app.add_blueprint_list(blueprints or config.BLUEPRINTS)
    app.setup()

    return app