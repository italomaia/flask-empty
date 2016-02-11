# -*- coding:utf-8 -*-

from flask.ext.script import Command, Option, prompt_bool

import os


class CreateDB(Command):
    """
    Creates database using SQLAlchemy
    """

    def run(self):
        try:
            from database import create_all

            create_all()
        except ImportError:
            print("Please, make sure database.create_all exists in order to create a db.")


class DropDB(Command):
    """
    Drops database using SQLAlchemy
    """

    def run(self):
        try:
            from database import drop_all

            drop_all()
        except ImportError:
            print("Please, make sure database.drop_all exists in order to drop a db.")


class Apps(Command):
    """
    Command to handle blueprints within your project
    """
    APPS_FOLDER = 'apps'
    NEW_APP = False

    @staticmethod
    def normalize_path(name):
        return os.path.normpath(name).replace(" ", "_").lower()

    @property
    def requirements(self):
        if self._requirements is None:
            try:
                try:
                    self._requirements = open('requirements/common.txt').read()
                except FileNotFoundError:
                    self._requirements = open('requirements.txt').read()
            except FileNotFoundError:
                self._requirements = ''
            finally:
                self._requirements = self._requirements.lower()
        return self._requirements

    def get_options(self):
        return [
            Option('--new', '-n', dest='new_app', nargs='?',
                   default=self.NEW_APP, const='store_true'),
            Option('--name', dest='name', type=str, nargs='?'),
            Option('--folder', '-f', dest='folder',
                   default=self.APPS_FOLDER, type=str, nargs='?'),
        ]

    def run(self, **kwargs):
        apps_folder = os.path.abspath(kwargs['folder'])
        name = kwargs['name'] or prompt('How will you call it?')
        path_name = self.normalize_path(name)
        app_path = os.path.join(apps_folder, path_name)

        if os.path.exists(app_path):
            print('%s already exists. Exiting.' % app_path)
            exit()

        os.mkdir(app_path)
        os.mkdir(os.path.join(app_path, 'templates'))
        os.mkdir(os.path.join(app_path, 'templates', path_name))

        # empty __init__.py
        with open(os.path.join(app_path, '__init__.py'), 'w'):
            pass

        with open(os.path.join(app_path, 'models.py'), 'w') as file:
            if 'flask-sqlalchemy' in self.requirements:
                file.write("from database import db\n\n")

            if 'flask-mongoengine' in self.requirements:
                file.write("from database import nosql\n\n")

        if 'flask-wtf' in self.requirements:
            with open(os.path.join(app_path, 'forms.py'), 'w') as file:
                file.write('from from flask_wtf import Form\n\n')

        with open(os.path.join(app_path, 'views.py'), 'w') as file:
            file.write(""
                "from flask import Blueprint\n"
                "from flask import render_template, flash, redirect, url_for\n\n"
                "app = Blueprint('%(name)s', __name__, template_folder='templates')\n\n"
                % {'name': name}
            )


class Test(Command):
    """
    Run tests
    """

    verbosity = 2
    failfast = False

    def get_options(self):
        return [
            Option('--verbosity', '-v', dest='verbosity',
                    type=int, default=self.verbosity),
            Option('--failfast', dest='failfast',
                    default=self.failfast, action='store_false')
        ]

    def run(self, **kwargs):
        import sys
        import glob
        import unittest

        exists = os.path.exists
        isdir = os.path.isdir
        join = os.path.join

        project_path = os.path.abspath(os.path.dirname('.'))
        sys.path.insert(0, project_path)

        # our special folder for blueprints
        if exists('apps'):
            sys.path.insert(0, join('apps'))

        loader = unittest.TestLoader()
        all_tests = []

        if exists('apps'):
            for path in glob.glob('apps/*'):
                if isdir(path):
                    tests_dir = join(path, 'tests')

                    if exists(join(path, 'tests.py')):
                        all_tests.append(loader.discover(path, 'tests.py'))
                    elif exists(tests_dir):
                        all_tests.append(loader.discover(tests_dir, pattern='test*.py'))

        if exists('tests') and isdir('tests'):
            all_tests.append(loader.discover('tests', pattern='test*.py'))
        elif exists('tests.py'):
            all_tests.append(loader.discover('.', pattern='tests.py'))

        test_suite = unittest.TestSuite(all_tests)
        unittest.TextTestRunner(**kwargs).run(test_suite)
