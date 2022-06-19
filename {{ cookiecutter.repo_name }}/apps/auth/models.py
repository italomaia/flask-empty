from extensions import db
from flask_security.models import fsqla_v2 as fsqla

# design here will probably change along the way
fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    pass

class User(db.Model, fsqla.FsUserMixin):
    pass
