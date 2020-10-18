# coding:utf-8


class HttpMixin:
    """
    Configures jinja2, default http errors and a basic index view.
    Useful for traditional http applications.
    """

    def configure_template_extensions(self):
        """
        Add jinja2 extensions here
        """
        # 'do' extension. see: http://jinja.pocoo.org/docs/extensions/#expression-statement  # noqa
        self.jinja_env.add_extension('jinja2.ext.do')

    def configure_error_handlers(self):
        from flask import render_template

        @self.errorhandler(403)
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
            return render_template("http/access_forbidden.html"), 403

        @self.errorhandler(404)
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
            return render_template("http/page_not_found.html"), 404

        @self.errorhandler(405)
        def method_not_allowed_page(error):
            """
            The method specified in the Request-Line is not allowed for the resource
            identified by the Request-URI. The response MUST include an Allow header
            containing a list of valid methods for the requested resource.
            """
            return render_template("http/method_not_allowed.html"), 405

        @self.errorhandler(500)
        def server_error_page(error):
            return render_template("http/server_error.html"), 500
