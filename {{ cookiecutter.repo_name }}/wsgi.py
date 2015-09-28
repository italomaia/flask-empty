# coding:utf-8

from main import app_factory
import config

app = app_factory(config.Config, config.project_name)