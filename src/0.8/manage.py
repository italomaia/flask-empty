# -*- coding:utf-8 -*-

from flask.ext import script

if __name__ == "__main__":
    from main import app_factory
    import config

    app = app_factory(config.Dev)
    manager = script.Manager(app)
    manager.run()
