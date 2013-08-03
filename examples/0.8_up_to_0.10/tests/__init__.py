# -*- coding:utf-8 -*-

from unittest import TestCase

class BaseTestCase(TestCase):
    def setUp(self):
        import config
        from main import app_factory
        from database import create_all

        self.app = app_factory(config.Testing)
        self.client = self.app.test_client()
        create_all()

    def tearDown(self):
        from database import drop_all, remove_session
        drop_all()
        remove_session()
