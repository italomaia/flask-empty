# -*- coding:utf-8 -*-

from flask.ext import script

import commands

if __name__ == "__main__":
    from main import app_factory
    import config

    manager = script.Manager(app_factory)
    manager.add_option("-n", "--name", dest="app_name", required=False, default=config.project_name)
    manager.add_option("-c", "--config", dest="config", required=False, default=config.Dev)
    manager.add_command("test", commands.Test())
    manager.add_command("apps", commands.Apps())
    {%- if cookiecutter.use_sql == 'yes' %}
    manager.add_command("db-create", commands.CreateDB())
    manager.add_command("db-drop", commands.DropDB())
    {%- endif %}

    manager.run()
