# -*- coding:utf-8 -*-

from tests import BaseTestCase as TestCase
from flask import url_for


def build_post(commit=True):
    from blog.models import Post
    from database import db

    post = Post('some title', 'some content')

    if commit:
        db.session.add(post)
        db.session.commit()

    return post


class TestUrlBuild(TestCase):
    app_prefix = ''

    def test_build_index_url(self):
        self.assertEqual(url_for('blog.list_posts_view'), '/')

    def test_build_add_post_url(self):
        self.assertEqual(url_for('blog.add_post_view'), '/add/')

    def test_build_post_url(self):
        post = build_post()
        self.assertEqual(url_for('blog.post_view', slug=post.slug), '/%s/' % post.slug)

    def test_post_permalink_build(self):
        post = build_post()
        self.assertEqual(post.absolute_url(), '/%s/' % post.slug)