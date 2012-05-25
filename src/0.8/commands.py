# -*- coding:utf-8 -*-

from flask.ext.script import Command, Option, prompt_bool

import os
import config


class CreateDB(Command):
	"Creates sqlalchemy database"
	
	def run(self):
		from database import create_all
		create_all()
		
		
class DropDB(Command):
	"Drops sqlalchemy database"
	
	def run(self):
		from database import drop_all
		drop_all()


class Test(Command):
    "Run tests."

    start_discovery_dir = "tests"

    def get_options(self):
        return [
            Option('--start_discover', '-s', dest='start_discovery',
                help='Pattern to search for features',
                default=self.start_discovery_dir),
        ]

    def run(self, start_discovery):
        import unittest

        if os.path.exists(start_discovery):
            argv = [config.project_name, "discover"]
            argv += ["-s", start_discovery]

            unittest.main(argv=argv)
        else:
            print("Directory '%s' was not found in project root." % start_discovery)


