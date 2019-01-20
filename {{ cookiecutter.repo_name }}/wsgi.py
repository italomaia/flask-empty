# coding:utf-8

from main import app_factory
from config import project_name
import os

config_obj_path = os.environ['FLASK_CONFIG_DEFAULT']
app = app_factory(config_obj_path, project_name)
