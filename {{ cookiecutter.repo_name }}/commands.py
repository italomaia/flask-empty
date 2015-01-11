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
        except ImportError, e:
            print "Please, make sure database.create_all exists in order to create a db."


class DropDB(Command):
    """
    Drops database using SQLAlchemy
    """

    def run(self):
        try:
            from database import drop_all

            drop_all()
        except ImportError, e:
            print "Please, make sure database.drop_all exists in order to drop a db."


class Test(Command):
    """
    Run tests
    """

    verbosity = 2
    failfast = False

    def get_options(self):
        return [
            Option('--verbosity', '-v', dest='verbose',
                    type=int, default=self.verbosity),
            Option('--failfast', dest='failfast',
                    default=self.failfast, action='store_false')
        ]

    def run(self, verbosity, failfast):
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
        unittest.TextTestRunner(
            verbosity=verbosity, failfast=failfast).run(test_suite)
