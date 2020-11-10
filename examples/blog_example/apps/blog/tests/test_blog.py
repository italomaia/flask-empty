# -*- coding:utf-8 -*-

from utils import BaseTestCase as TestCase
from flask import url_for
from urllib.parse import urlparse


def build_post(commit=True):
    from blog.models import Post
    from extensions import db

    post = Post('some title', 'some content')

    if commit:
        db.session.add(post)
        db.session.commit()

    return post


class TestUrlBuild(TestCase):
    app_prefix = ''

    def test_build_index_url(self):
        url = urlparse(url_for('blog.list_posts_view'))

        self.assertEqual(url.path, '/blog/')

    def test_build_add_post_url(self):
        url = urlparse(url_for('blog.add_post_view'))

        self.assertEqual(url.path, '/blog/add/')

    def test_build_post_url(self):
        post = build_post()
        url = urlparse(url_for('blog.post_view', slug=post.slug))

        self.assertEqual(url.path, '/blog/%s/' % post.slug)

    def test_post_permalink_build(self):
        post = build_post()
        url = urlparse(post.absolute_url())

        self.assertEqual(url.path, '/blog/%s/' % post.slug)