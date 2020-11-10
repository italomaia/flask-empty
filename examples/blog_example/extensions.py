import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security
from flask_admin import Admin

toolbar = None

if os.environ['FLASK_CONFIG_DEFAULT'] == 'Dev':
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension()


db = SQLAlchemy()
migrate = Migrate(db=db)
admin = Admin()
security = Security()


def security_init_kwargs():
    """
    **kwargs arguments passed down during security extension initialization by
    "empty" package.
    """
    return dict()
