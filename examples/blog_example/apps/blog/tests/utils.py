# -*- coding:utf-8 -*-

from unittest import TestCase


class BaseTestCase(TestCase):
    def setUp(self):
        import config
        from main import app_factory
        from extensions import db

        self.app = app_factory(config.Test, config.project_name)
        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        from extensions import db

        db.drop_all()
        db.remove_session()