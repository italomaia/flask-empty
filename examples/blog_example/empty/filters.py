"""Extra Jinja2 filters."""

from flask import current_app


def format_date(date):
    config = current_app.config
    date_format = config.get('DATE_FORMAT', '%Y/%m/%d')
    return date.strftime(date_format)


def format_datetime(datetime):
    config = current_app.config
    datetime_format = config.get('DATETIME_FORMAT', '%Y/%m/%d %H:%M')
    return datetime.strftime(datetime_format)
