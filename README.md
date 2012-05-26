Flask Empty
===========
Flask-Empty is a simple **flask skeleton** project for fast flask prototype. Just 
clone de project and copy the example you would like the most.

Usage
=====
Clone the repository. In src/ folder, copy somewhere else the flask-version example that you would like
to work with. Rename the folder to your project name. Change it to your needs = ]

Configuring
===========
src/config.py has some pre-configured flask configuration classes ready for you. They're are all self explanatory.
Dev is used by default, while Testing is used only when running tests. Config is a more general configuration.
Extend it to create your production config.

Templates
=========
There are some error templates bundled with flask-empty by default. All empty right now.

Blueprints
==========
Add your blueprints through the src/config.BLUEPRINTS. A blueprint can be added using the path to the
associated Blueprint instance like **blog.views.app** where blog.views are the module path and app is the
variable name.

SQLAlchemy
==========
Flask-Empty comes with some Flask-SQLAlchemy configurations ready for you. Just uncomment some lines in your **main.py**
and **database.py** files.

_ps: your models will only be created if they are imported somewhere in your application. By **somewhere**, try the_
_same module where your Blueprint instance is defined._

Examples
========
If my explanation above is as crappy as I think it is, you're gonna want/need to take a look at **examples/**. They
are a very nice starting point to learn how to configure your project.

