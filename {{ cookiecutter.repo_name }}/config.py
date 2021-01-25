{%- set uses_cockroachdb = cookiecutter.use_sql_cockroachdb in ('y', 'yes') -%}
{%- set uses_postgres = cookiecutter.use_sql_postgres in ('y', 'yes') -%}
{%- set uses_sqlite = cookiecutter.use_sql_sqlite in ('y', 'yes') -%}
{%- set uses_mysql = cookiecutter.use_sql_mysql in ('y', 'yes') -%}
{%- set uses_sql = uses_cockroachdb
    or uses_postgres
    or uses_mysql
    or uses_sqlite -%}
{%- set uses_mongodb = cookiecutter.use_nosql_mongodb in ('y', 'yes') -%}
{%- set uses_socketio = cookiecutter.use_socketio in ('yes', 'y') -%}
{%- set uses_static_files = cookiecutter.serve_static_files in ('yes', 'y') -%}

import os
import logging

from datetime import timedelta
from typing import Dict
from typing import List

project_name = "{{ cookiecutter.repo_name }}"


{%- if uses_postgres or uses_cockroachdb %}
SQLALCHEMY_DATABASE_URI_TMPL = "postgresql+psycopg2://%(user)s:%(passwd)s@%(host)s/%(name)s"
{%- elif uses_mysql %}
SQLALCHEMY_DATABASE_URI_TMPL = "mysql+mysqldb://%(user)s:%(passwd)s@%(host)s/%(name)s"
{%- elif uses_sqlite %}
SQLALCHEMY_DATABASE_URI_TMPL = "sqlite:////tmp/%(name)s.sqlite"
{% endif %}


# base config class; extend it to your needs.
class Config(object):
    # see http://flask.pocoo.org/docs/1.0/config/#environment-and-debug-features
    ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'

    # use TESTING mode?
    TESTING = False

    # use server x-sendfile?
    USE_X_SENDFILE = False

    # should be the hostname of your project
    HOST = os.getenv('HOST', '')  # create an alias in /etc/hosts for dev
    # useful for development/testing mode
    # necessary if non-standard port is being used
    HOST_PORT = os.getenv('HOST_PORT', '')
    # we need to append the host port to the server_name if it is non-standard
    SERVER_NAME_EXTRA = len(HOST_PORT) and '' or (":" + HOST_PORT)
    # SERVER_NAME contains the hostname and port (if non-default)
    SERVER_NAME = HOST + SERVER_NAME_EXTRA

    # use to set werkzeug / socketio options, if needed
    # SERVER_OPTIONS = {}

    {%- if uses_sql %}
    # DATABASE CONFIGURATION

    # Postgres: psycopg2 and pg8000
    # - f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # - f"postgresql+pg8000://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # MySQL: mysqlclient and PyMySQL
    # - f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # - f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # Oracle: cx_oracle (not advised)
    # - DB_NAME here is sidname
    # - f"oracle://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # - DB_NAME here is tnsname
    # - f"oracle+cx_oracle://{DB_USER}:{DB_PASS}@{DB_NAME}"
    # Mysql Server: pyodbc or pymssql or mysqlclient (default)
    # - DB_NAME here is mydsn
    # - f"mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_NAME}"
    # - f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    # - f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

    DB_USER = os.getenv('DB_USER', '')
    DB_PASS = os.getenv('DB_PASS', '')
    DB_HOST = os.getenv('DB_HOST', '')  # plus port, if non-default
    DB_NAME = os.getenv('DB_NAME', '')

    # default database connection
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_TMPL % {
        'user': DB_USER,
        'passwd': DB_PASS,
        'host': DB_HOST,
        'name': DB_NAME
    }

    # set this up case you need multiple database connections
    SQLALCHEMY_BINDS: Dict = {}

    # log all the statements issued to stderr?
    SQLALCHEMY_ECHO = DEBUG
    # track and emit signals on object modification?
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    {%- endif %}{# end if uses_sql  #}

    {%- if uses_mongodb %}
    # mongodb connection configuration;
    # be sure to use username and password in production
    MONGODB_DB = os.getenv('MONGODB_NAME', project_name)
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'localhost')
    MONGODB_PORT = os.getenv('MONGODB_PORT', '')
    MONGODB_USER = os.getenv('MONGODB_USER', '')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', '')

    {%- endif %}
    WTF_CSRF_ENABLED = True
    # import os; os.urandom(24)
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "secret")

    # LOGGING
    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "/var/tmp/app.%s.log" % project_name
    LOG_LEVEL = logging.INFO
    # used by logging.Formatter
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s"

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # EMAIL CONFIGURATION
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = os.getenv("FLASK_MAIL_SERVER", "localhost")
    MAIL_PORT = int(os.getenv("FLASK_MAIL_PORT", "25"))
    MAIL_USE_TLS = os.getenv("FLASK_MAIL_USE_TLS", "") == "1"
    MAIL_USE_SSL = os.getenv("FLASK_MAIL_USE_SSL", "") == "1"
    MAIL_USERNAME = os.getenv("FLASK_MAIL_USERNAME", None)
    MAIL_PASSWORD = os.getenv("FLASK_MAIL_PASSWORD", None)
    DEFAULT_MAIL_SENDER = os.getenv(
        "FLASK_DEFAULT_MAIL_SENDER",
        "example@%s.com" % project_name
    )

    # these are the modules preemptively
    # loaded for each app
    LOAD_MODULES_EXTENSIONS = [
        'views',
        'models',
        'admin',
        'api',
        'schemas'
    ]

    # add below the module path of extensions
    # you wish to load
    EXTENSIONS = [
        {%- if uses_sql %}
        'extensions.db',
        'extensions.migrate',
        {%- endif %}
        {%- if uses_mongodb %}
        'extensions.nosql',
        {%- endif %}
        {%- if cookiecutter.use_security in ('yes', 'y') %}
        'extensions.security',
        {%- endif %}
        {%- if cookiecutter.use_admin in ('yes', 'y') %}
        'extensions.admin',
        {%- endif %}
        {%- if cookiecutter.use_rest in ('yes', 'y') %}
        'extensions.ma',
        'extensions.glue',
        {%- endif %}
        {%- if uses_socketio %}
        'extensions.io',
        {%- endif %}
        {%- if uses_static_files %}
        'extensions.compress',
        {%- endif %}
    ]

    # see example/ for reference
    # ex: BLUEPRINTS = ['blog']  # where `blog` is a Blueprint instance
    # ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where `blog` is a Blueprint instance
    BLUEPRINTS: List = []


# config class for development environment
class Dev(Config):
    MAIL_DEBUG = True
    EXTENSIONS = Config.EXTENSIONS + [
        'extensions.toolbar'
    ]
    # uses sqlite by default
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/%s.db' % Config.DB_NAME


# config class used during tests
class Test(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    {%- if uses_sql %}
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_TMPL % {
        'user': Config.DB_USER,
        'passwd': Config.DB_PASS,
        'host': Config.DB_HOST,
        'name': "%s-test" % Config.DB_NAME
    }
    {%- endif %}

    {%- if uses_mongodb %}
    # mongodb connection configuration;
    # be sure to use username and password in production
    MONGODB_DB = "%s-test" % Config.MONGODB_NAME
    {%- endif %}
