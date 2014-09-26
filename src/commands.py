# -*- coding:utf-8 -*-

from flask.ext.script import Command, Option, prompt_bool

import os
import config


class CreateDB(Command):
    """
    Creates database using SQLAlchemy
    """

    def run(self):
        from database import create_all

        create_all()


class DropDB(Command):
    """
    Drops database using SQLAlchemy
    """

    def run(self):
        from database import drop_all

        drop_all()


class Test(Command):
    """
    Run tests
    """

    use_coverage = False
    no_capture = False
    verbose = False

    def get_options(self):
        return [
            Option('--with-coverage', '-c', dest='use_coverage', action='store_true',
                    help='Use coverage?', default=self.use_coverage),
            Option('--no-capture', '-s', dest='no_capture', action='store_true',
                    default=self.no_capture),
            Option('--verbose', '-v', dest='verbose', action='store_true',
                    default=self.verbose)
        ]

    def run(self, use_coverage, no_capture, verbose):
        import sys
        import nose

        project_path = os.path.abspath(os.path.dirname('.'))
        sys.path.insert(0, project_path)

        argv = []

        if verbose:
            argv += ['-v']

        if no_capture:
            argv += ['-s']

        if use_coverage:
            argv += ['--with-coverage']

        if os.path.exists('apps'):
            argv += ['-w', 'apps']
        elif os.path.exists('tests'):
            argv += ['-w', 'tests']

        nose.main(argv=argv)
