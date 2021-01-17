# coding:utf-8

import os
import click

try:
    FileNotFoundError  # only available with python3
except NameError:
    # workaround
    FileNotFoundError = IOError

TEST_CMD_HELP = 'Run tests defined for your blueprints. Extra arguments go to test runner.'

APPS_FOLDER = 'apps'


@click.command('new-app', help='creates a new blueprint app')
@click.argument('name', required=False)
@click.option(
    '-t', '--with-templates',
    default=False, is_flag=True, show_default=True,
    help='create templates folder for blueprint')
def new_app(name, with_templates):
    """
    Command to handle blueprints within your project
    """

    if name is None:
        # useful with makefiles
        name = input('provide new app name: ')

        if len(name) == 0:
            print("name is missing; nothing to do")
            exit(1)

    try:
        try:
            # supports split requirements
            requirements = open('requirements/common.txt').read().lower()
        except FileNotFoundError:
            requirements = open('requirements.txt').read().lower()
    except FileNotFoundError:
        requirements = ''

    apps_folder = os.path.abspath(APPS_FOLDER)
    path_name = os.path.normpath(name).replace(" ", "_").lower()
    app_path = os.path.join(apps_folder, path_name)

    if os.path.exists(app_path):
        print('%s already exists. Cannot create another. Sorry :T' % app_path)
        exit()

    os.mkdir(app_path)

    if with_templates:
        os.mkdir(os.path.join(app_path, 'templates'))
        os.mkdir(os.path.join(app_path, 'templates', path_name))

    # empty __init__.py
    with open(os.path.join(app_path, '__init__.py'), 'w') as fs:
        fs.write("from .views import app")

    with open(os.path.join(app_path, 'models.py'), 'w') as fs:
        if 'flask-sqlalchemy' in requirements:
            fs.write("from extensions import db\n\n")

        if 'flask-mongoengine' in requirements:
            fs.write("from extensions import nosql\n\n")

    if 'flask-wtf' in requirements:
        with open(os.path.join(app_path, 'forms.py'), 'w') as fs:
            fs.write('from flask_wtf import FlaskForm\n\n')

    with open(os.path.join(app_path, 'views.py'), 'w') as fs:
        fs.write(
            "# keep this file even if you don't need traditional views\n"
            "# as it holds the blueprint app instance\n"
            "from flask import Blueprint\n"
            "from flask import render_template, flash, redirect, url_for\n\n"  # noqa
            "app = Blueprint('%(name)s', __name__, template_folder='templates')\n\n"  # noqa
            % {'name': name})

    print(
        f'App created under {APPS_FOLDER}. '
        f'Remember to add it to BLUEPRINTS in your configuration.'
    )


@click.command('test', context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
), help=TEST_CMD_HELP)
@click.option('-f', '--failfast', default=False, is_flag=True, help='test runner option')  # noqa
@click.option('-v', '--verbosity', type=int, default=1, help='test runner option [0|1|2]')  # noqa
@click.option('-w', '--warnings', default=None, help='test runner option [default|always]')  # noqa
def test_cmd(failfast, verbosity, warnings):
    """
    Run tests
    """

    import sys
    import glob
    import unittest

    exists = os.path.exists
    isdir = os.path.isdir
    join = os.path.join

    project_path = os.path.abspath(os.path.dirname('.'))
    sys.path.insert(0, project_path)

    # our special folder for blueprints
    if exists(APPS_FOLDER):
        sys.path.insert(0, join(APPS_FOLDER))

    loader = unittest.TestLoader()
    all_tests = []

    # tests within apps folder
    if exists(APPS_FOLDER):
        for path in glob.glob('%s/*' % APPS_FOLDER):
            if isdir(path):
                tests_dir = join(path, 'tests')

                if exists(join(path, 'tests.py')):
                    all_tests.append(loader.discover(path, 'tests.py'))
                elif exists(tests_dir):
                    all_tests.append(loader.discover(tests_dir, pattern='test*.py'))  # noqa

    # project level tests
    if exists('tests') and isdir('tests'):
        all_tests.append(loader.discover('tests', pattern='test*.py'))
    elif exists('tests.py'):
        all_tests.append(loader.discover('.', pattern='tests.py'))

    test_suite = unittest.TestSuite(all_tests)
    unittest.TextTestRunner(
        warnings=warnings,
        failfast=failfast,
        verbosity=verbosity
    ).run(test_suite)
