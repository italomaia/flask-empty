Changelog
=========

Version 0.6.3

- added `flask-migrate` commands to makefile
- added `wtforms-sqlalchemy` as an optional dependecy
- `new-app` command now uses FlaskForm in forms.py
- added docs on makefile
- updated old docs (.venv is not used anymore)
- `compress` should be working now

Version 0.6.2

- fixed new-app command import
- if sqlalchemy support is enabled, sqlalchemy-utils is added to requirements
- added vscode to gitignore
- "name" is now optional for the "new-app" command
- added new-app to Makefile
- added app import to \_\_init\_\_ blueprint files

Version 0.6.1

- added .gitignore
- added .editorconfig
- added sqlite as default db for dev
- added Makefile to make things easier
- added static files folder
- added support for transpiling with flask-static-compress
- changed some logs and comments
- changed default host value

Version 0.6.0

- fixed/updated blog example
- fixed cockroachdb support
- fixed db configuration

Version 0.5.9

- bugfix for missing uses_cocroachdb variable when building the Dockerfile
- added json friendly globals true, false and null + docs + tests
- pytest is now a dependency

Version 0.5.8

- Support for postgres AND mysql configuration out of the box
- Replaced flask-security package with flask-security-too given the former no longer has support
- Updated Dockerfile, so all libs can be built out of the box

Version 0.5.7.1

- Fixed typo in cookiecutter template; kudos to **plars**

Version 0.5.7

- Fixed socketio support
- Added out-of-the-box support for postgres, mysql and cockroachdb configurations
- Updated mongodb configuration

Version 0.5.6

- Fixed flask-security initialization function
- Changed flask-security-fork requirement by flask-security
- Refactored extensions module
- Added "y" as an cookiecutter option for "yes"

Version 0.5.5

- Fixed options for wsgi when running with socketio
- Added SERVER_OPTIONS to config

Version 0.5.4

- Fixed create_index_view check
- Fixed use_socketio check

Version 0.5.3.1

- Fixed WTF integration (kudos to ivopanjos)
- Added warning when FLASK_CONFIG_DEFAULT is not provided

Version 0.5.3

- Fixed support for flask-socketio (support for flask run was dropped)

Version 0.5.2

- Updated cookiecutter variable names
- `use_admin` no longer breaks project
- Removed .env
- **config.py** now uses environment variables for most options
- Added instructions for database uri

Version 0.5.1

- Added docker support
- Updated configuration to use FLASK_ENV

Version 0.5

- Updated commands to use click (flask-script is no more)
- Empty package is now used
- Added docs to newly created projects
- Random fixes here and there =3

Version 0.3.2

- Changed cookiecutter input to ask wether the app will be rest or _plain_ http.
- New default dependencies.

Version 0.3.1

- Still quite unsure

Version 0.3

- I'm quite unsure
