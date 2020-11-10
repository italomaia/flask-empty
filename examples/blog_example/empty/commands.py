import click


def routes():
    """
    Lists each available route in the project.
    """
    from flask import url_for, current_app
    from urllib.parse import unquote

    output = []
    for rule in current_app.url_map.iter_rules():

        options = dict([
            (arg, "[{0}]".format(arg))
            for arg in rule.arguments
        ])

        url = url_for(rule.endpoint, **options)
        methods = ','.join(rule.methods)
        line = unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        click.echo(line)
