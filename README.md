Flask Empty
===========
Flask-Empty is a simple **flask skeleton** project for fast flask prototyping. Just
clone de project and copy the example you like the most.

Usage
=====
Clone the repository. In **src/** folder, copy somewhere else the flask-version example that you want
to work with. Rename the folder to your project name. Change configurations to your needs and have fun! = ]

Configuring
===========
**src/config.py** has some pre-configured flask configuration classes for you. They're are all self explanatory.
**Dev** is used by default with the runserver command, while **Testing** is used only when running tests. **Config**
is a more general configuration. You can extend any of these classes to create your production config or some
other special configuration.

Note that the Flask-Script option, -d (disable debug) does not work as expected in Flask-Empty. If you want
to start a non-debug internal server instance, use the **config.Config** configuration or write your own. Example:

   # loads config.Config configuration, which has DEBUG=False
   # -r is the Flask-Script option for internal server no-reload
   python manage.py -r -c Config

Templates
=========
There are some error templates bundled with flask-empty by default. All empty right now. Just fill them up for
your project.

Blueprints
==========
Add your blueprints through the src/config.ConfigClass.BLUEPRINTS. A blueprint can be added using the path to the
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
