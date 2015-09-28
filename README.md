Flask Empty
===========

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/italomaia/flask-empty?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Flask-Empty is a simple **flask boilerplate** for fast prototyping. Just
use cookiecutter and create a new project in no time.

```shell
# if cookiecutter is not installed
sudo pip install cookiecutter

# using cookiecutter // linux/Mac
cookiecutter https://github.com/italomaia/flask-empty

# answer the prompt and you're done!
```

Setup
=====

You're advised to use virtualenvwrapper from here on. Install it like this:

```
pip install virtualenvwrapper
```

Create a virtual environment for you project and install the adequate requirements.

```
mkvirtualenv my_project
pip install -r requirements/dev.txt  # dev environment if local
pip install -r requirements/prod.txt  # prod environment if server
```

You're advised to change the requirements files according to your needs.

Important files to be aware of
==============================

### project/config.py

**config.py** has some pre-set configuration classes for you to meddle with. They're are all self explanatory
and commented.  

**main.py** extend flask application behavior through Empty class, which inherit from Flask class. Need to setup
extensions, index view, context processors? (see also **empty.py**)

**database.py** setup your database library there. There is some commented code for sqlalchemy support out of the box.

**rename_me.ini** rename it to your project name. It is the configuration file to use
with [uwsgi](https://github.com/unbit/uwsgi). Use it like this:

```
uwsgi --ini your_project.ini
```

**manage.py** and **commands.py** add to manage.py all the commands from commands.py that you want available using
 commandline. See available commands with **python manage.py**

## Heroku

Empty comes with a pre-configured procfile and heroku() wrapper for app_factory. No setup required.

## Observations

Note that the Flask-Script option, -d (disable debug) does not work as expected in Flask-Empty. If you want
to start a non-debug internal server instance, use the **config.Config** configuration or write your own. Example:

```python
# loads config.Config configuration, which has DEBUG=False
# -r is the Flask-Script option for internal server no-reload
python manage.py -r -c Config
```

If [environment config named APP_CONFIG is set](http://flask.pocoo.org/docs/config/#configuring-from-files),
it will be used, overwriting any other set configuration.

Other topics
============

## Templates

There are some error templates bundled with flask-empty by default. All empty right now. Just fill them up for
your project.

## Macros

You can use the jinja2 macros available in **templates/macros** to easily integrate your jinja2 templates with
flask extensions like wtforms and commons tasks like showing flash messages. Available macros, **formhelpers**
and **flashing** are very useful.

## Blueprints

Add your blueprints using **src/config.Config.BLUEPRINTS** as documented in the file itself. A blueprint can be add
using the path to the Blueprint or a tuple. Make sure your blueprint has a views.py and
it has a **app** Blueprint instance and you're ready to go. If unsure, check out **flask-empty/blueprint/**
for an empty blueprint example. You can also copy **flask-empty/blueprint/** to create blueprints.

With flask-empty, blueprints can live in the project root or in a special folder called **apps** in the project root.

## SQLAlchemy

Flask-Empty comes with some Flask-SQLAlchemy configurations ready for you. Just extend
your **main.App.configure_database** like this:

```
class App(Empty):
    def configure_database(self):
        super(App, self).configure_database()
        from database import db
        db.app = self
        db.init_app(self)
```

and uncomment **database.py**.

_ps: currently, create_db will only create your models will if they are imported somewhere in your application.
By **somewhere**, try the *same module where your Blueprint instance is defined*.

Examples
========
If my explanation above is as crappy as I think it is, you're gonna want/need to take a look at **examples/**. They
are a very nice starting point to learn how to configure your project. Wort-case-scenario, just copy it, rename it,
configure it and be happy!

FAQ
===
**Is flask-empty _boilerplate_ compatible with flask 0.x? Cuz' that's what my app uses.**

Right now, flask-empty is a very simple project where many good practices and code examples were glued together.
Until recently I was focused in keeping backward compatibility with flask 0.8. Well, that goal is no more.
 Flask-empty will be compatible with the latest version of Flask and, by chance, with previous versions in case
 there is no backward incompatibility from any supported plugin or flask itself. Things will be easier this way.

**So, which is the oldest version where flask-empty works?**

In my last test, version 0.8 but no guarantees here.

**I think flask-empty should have _this_ and _that_ configured by default. Will you add support?**

My current goals are:

* Make flask-empty real easy to start a project with
* Keep things simple and robust

If your suggestion is simple, **VERY** useful and with little overhead, I'll probably consider adding it to the
project. If you make the code and send a pull request, then I'll consider it real hard. Now, if your suggestion is
 rejected or advised in a different approach, don't ge sad (you're awesome ;).

**I just made a cool example with flask-empty and want to add it to examples.**

Pull request it for evaluation ;)
Just keep in mind that good examples should be short (not really...) and focused in it's showcase.
