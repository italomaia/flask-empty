# -*- coding:utf-8 -*-

from flask import Flask, render_template


def __import_blueprint(blueprint_str):
    split = blueprint_str.split('.')
    module_path = '.'.join(split[0: len(split) - 1])
    variable_name = split[-1]
    mod = __import__(module_path, fromlist=[variable_name])
    return getattr(mod, variable_name)


def config_str_to_obj(cfg):
    if isinstance(cfg, basestring):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(config, app_name=None, blueprints=None):
    app_name = app_name or __name__
    app = Flask(app_name)

    config = config_str_to_obj(config)
    configure_app(app, config)
    configure_blueprints(app, blueprints or config.BLUEPRINTS)
    configure_error_handlers(app)
    configure_database(app)
    configure_context_processors(app)
    configure_template_filters(app)
    configure_extensions(app)
    configure_before_request(app)
    configure_views(app)

    return app


def configure_app(app, config):
    app.config.from_object(config)
    app.config.from_envvar("APP_CONFIG", silent=True)  # avaiable in the server


def configure_blueprints(app, blueprints):
    for blueprint_config in blueprints:
        blueprint, kw = None, {}

        if (isinstance(blueprint_config, basestring)):
            blueprint = blueprint_config
        elif (isinstance(blueprint_config, tuple)):
            blueprint = blueprint_config[0]
            kw = blueprint_config[1]

        blueprint = __import_blueprint(blueprint)
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
    "Database configuration should be set here"
    # uncomment for sqlalchemy support
    # from database import db
    # db.app = app
    # db.init_app(app)


def configure_context_processors(app):
    "Modify templates context here"
    pass


def configure_template_filters(app):
    "Configure filters and tags for jinja"
    pass


def configure_extensions(app):
    "Configure extensions like mail and login here"
    pass


def configure_before_request(app):
    pass


def configure_views(app):
    "Add some simple views here like index_view"
    pass
