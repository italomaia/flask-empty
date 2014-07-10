# -*- config:utf-8 -*-

import logging
from datetime import timedelta

project_name = "yourprojectname"


class Config(object):
    # use DEBUG mode?
    DEBUG = False

    # use TESTING mode?
    TESTING = False

    # use server x-sendfile?
    USE_X_SENDFILE = False

    # DATABASE CONFIGURATION
    # see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
    SECRET_KEY = "secret"  # import os; os.urandom(24)

    # LOGGING
    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "/var/tmp/app.%s.log" % project_name
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s" # used by logging.Formatter

    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

    # see example/ for reference
    # ex: BLUEPRINTS = ['blog']  # where app is a Blueprint instance
    # ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where app is a Blueprint instance
    BLUEPRINTS = []


class Dev(Config):
    DEBUG = True
    MAIL_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////var/tmp/%s_dev.sqlite" % project_name


class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name