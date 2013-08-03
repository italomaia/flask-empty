# -*- coding:utf-8 -*-

from tests import BaseTestCase as TestCase
from flask import url_for

class TestBlogViews(TestCase):
    def test_index_view(self):
        url_path = url_for('blog.views.index_view')
        self.client.get(url_path)
