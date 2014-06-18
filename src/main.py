# -*- coding:utf-8 -*-

import os
import sys
import logging
from flask import Flask, render_template


# apps is a special folder where you can place your blueprints
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))


def __import_variable(blueprint_path, module, variable_name):
    path = '.'.join(blueprint_path.split('.') + [module])
    mod = __import__(path, fromlist=[variable_name])
    return getattr(mod, variable_name)


def config_str_to_obj(cfg):
    if isinstance(cfg, basestring):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(config, app_name, blueprints=None):
    app = Flask(app_name)

    config = config_str_to_obj(config)
    configure_app(app, config)
    configure_logger(app, config)
    configure_blueprints(app, blueprints or config.BLUEPRINTS)
    configure_error_handlers(app)
    configure_database(app)
    configure_context_processors(app)
    configure_template_extensions(app)
    configure_template_filters(app)
    configure_extensions(app)
    configure_before_request(app)
    configure_views(app)

    return app


def configure_app(app, config):
    """Loads configuration class into flask app"""
    app.config.from_object(config)
    app.config.from_envvar("APP_CONFIG", silent=True)  # available in the server


def configure_logger(app, config):
    log_filename = config.LOG_FILENAME

    # Create a file logger since we got a logdir
    log_file = logging.FileHandler(filename=log_filename)
    formatter = logging.Formatter(config.LOG_FORMAT)
    log_file.setFormatter(formatter)
    log_file.setLevel(config.LOG_LEVEL)
    app.logger.addHandler(log_file)
    app.logger.info("Logger started")


def configure_blueprints(app, blueprints):
    """Registers all blueprints set up in config.py"""
    for blueprint_config in blueprints:
        blueprint, kw = None, {}

        if isinstance(blueprint_config, basestring):
            blueprint = blueprint_config
        elif isinstance(blueprint_config, tuple):
            blueprint = blueprint_config[0]
            kw = blueprint_config[1]
        else:
            print "Error in BLUEPRINTS setup in config.py"
            print "Please, verify if each blueprint setup is either a string or a tuple."
            exit(1)

        blueprint = __import_variable(blueprint, 'views', 'app')
        app.register_blueprint(blueprint, **kw)


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        """
        The server understood the request, but is refusing to fulfill it.
        Authorization will not help and the request SHOULD NOT be repeated.
        If the request method was not HEAD and the server wishes to make public
        why the request has not been fulfilled, it SHOULD describe the reason for
        the refusal in the entity. If the server does not wish to make this
        information available to the client, the status code 404 (Not Found)
        can be used instead.
        """
        return render_template("access_forbidden.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        """
        The server has not found anything matching the Request-URI. No indication
        is given of whether the condition is temporary or permanent. The 410 (Gone)
        status code SHOULD be used if the server knows, through some internally
        configurable mechanism, that an old resource is permanently unavailable
        and has no forwarding address. This status code is commonly used when the
        server does not wish to reveal exactly why the request has been refused,
        or when no other response is applicable.
        """
        return render_template("page_not_found.html"), 404

    @app.errorhandler(405)
    def method_not_allowed_page(error):
        """
        The method specified in the Request-Line is not allowed for the resource
        identified by the Request-URI. The response MUST include an Allow header
        containing a list of valid methods for the requested resource.
        """
        return render_template("method_not_allowed.html"), 405

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("server_error.html"), 500


def configure_database(app):
    """
    Database configuration should be set here
    """
    # uncomment for sqlalchemy support
    # from database import db
    # db.app = app
    # db.init_app(app)


def configure_context_processors(app):
    """Modify templates context here"""
    pass


def configure_template_extensions(app):
    """
    Add jinja2 extensions here
    """
    # 'do' extension. see: http://jinja.pocoo.org/docs/extensions/#expression-statement
    app.jinja_env.add_extension('jinja2.ext.do')


def configure_template_filters(app):
    """Configure filters and tags for jinja"""
    pass


def configure_extensions(app):
    """Configure extensions like mail and login here"""
    pass


def configure_before_request(app):
    pass


def configure_views(app):
    """Add some simple views here like index_view"""
    pass
