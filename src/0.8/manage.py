# -*- coding:utf-8 -*-

from flask.ext import script

import commands

if __name__ == "__main__":
    from main import app_factory
    import config

    app = app_factory(config.Dev)
    manager = script.Manager(app)
    manager.add_command("test", commands.Test())
    manager.run()
