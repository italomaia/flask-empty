# -*- coding:utf-8 -*-

from unittest import TestCase
from empty import Empty


class BaseTestCase(TestCase):
    def setUp(self):
        import config
        from main import app_factory
        from extensions import db

        self.app: Empty = app_factory(config.Test, config.project_name)
        self.client = self.app.test_client()

        # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure/page/2
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        from extensions import db

        db.session.remove()
        db.drop_all()

        self.app_context.pop()
