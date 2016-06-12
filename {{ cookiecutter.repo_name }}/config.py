# -*- config:utf-8 -*-

import logging
from datetime import timedelta

project_name = "{{ cookiecutter.repo_name }}"


# base config class; extend it to your needs.
class Config(object):
    # use DEBUG mode?
    DEBUG = False

    # use TESTING mode?
    TESTING = False

    # use server x-sendfile?
    USE_X_SENDFILE = False

    {%- if cookiecutter.use_sql == 'yes' %}
    # DATABASE CONFIGURATION
    # see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = ""

    # DEBUG mode only!
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

    {% endif %}
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "secret"  # import os; os.urandom(24)

    # LOGGING
    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "/var/tmp/app.%s.log" % project_name
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s" # used by logging.Formatter

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

    LOAD_MODULES_EXTENSIONS = ['views', 'models']

    EXTENSIONS = [
        {% if cookiecutter.use_sql == 'yes' %}
        'extensions.db',
        {%- endif %}
        'extensions.toolbar',
    ]

    # see example/ for reference
    # ex: BLUEPRINTS = ['blog']  # where `blog` is a Blueprint instance
    # ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where `blog` is a Blueprint instance
    BLUEPRINTS = []


# config class for development environment
class Dev(Config):
    DEBUG = True  # we want debug level output
    MAIL_DEBUG = True
    SQLALCHEMY_ECHO = True  # we want to see sqlalchemy output
    SQLALCHEMY_DATABASE_URI = "sqlite:////var/tmp/%s_dev.sqlite" % project_name


# config class used during tests
class Test(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
