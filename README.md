Flask Empty
===========

**version 0.5.8**

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/italomaia/flask-empty?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Flask-Empty is a simple **flask boilerplate** for fast prototyping. Just
use cookiecutter and create a new project in no time.

```shell
# if cookiecutter is not installed
sudo pip install cookiecutter # or pip install --user cookiecutter

# using cookiecutter // linux/Mac
cookiecutter https://github.com/italomaia/flask-empty

# answer the prompt and you're done!
```

Getting Started
===============

You're advised to use venv from here on. In your project folder,
create and enable it like this:

```shell
python3 -m venv venv
. venv/bin/activate  # [.csh|.fish]

# install required packages
pip install -r requirements.txt

# loads env variables and runs the project in development mode
source .venv && flask run
```

Getting Started With Docker
===========================

Given you have up-to-date docker installed in your machine,
all you need to do is:

```shell
# build container image
docker build . -t my-project-name
# run container in development mode
docker run --rm -p 5000:5000 my-project-name
```

Environment Variables
=====================

Be aware that you might need to tweak the environment variables for production
mode. The are available at `.env` and `Dockerfile`. If using Docker,
you can even provide them inline.

Important files to be aware of
==============================

`<project>/extensions.py` all extension instances that need initialization should be available
here in order to have _Empty_ see and initialize them for you.

`<project>/config.py` is a pre-set configuration classes for you to meddle with. They're are all self explanatory
and commented.

`<project>/main.py` the _Empty_ class inherits from _empty.Empty_ which inherits from _flask.Flask_. Override it if you need to setup extensions, an index view, context processors, etc. It already has some sensitive defaults for most use cases. See https://github.com/italomaia/empty for all options.

`<project>/<project>.ini` is the configuration file used with
[uwsgi](https://github.com/unbit/uwsgi). Use it like this:

```
uwsgi --ini your_project.ini
```

`commands.py` adds few very useful commandline commands (...) to help your development productivity. Check available commands by running **flask**.

## Heroku

Empty comes with a pre-configured _procfile_ and _heroku()_ wrapper for _app_factory_. No setup required.

Other topics
============

## Templates

There are some error templates bundled with flask-empty by default. All empty right now. Just fill them up for your project.

## Macros

You can use the jinja2 macros available in `templates/macros` to easily integrate your jinja2 templates with
flask extensions like wtforms and commons tasks like showing flash messages. Available macros, **formhelpers** and **flashing** are very useful.

## Blueprints

You can create blueprints easily with `flask new-app <name>`. The will live, by default
at `apps` folder. Remember to configure your blueprints in `config.py` so that they
can be properly loaded.

# Supported Extensions

## Flask-SQLAlchemy

While creating your project, Flask-Empty will ask you if you wish to enable SQL support. Confirm if you do so
and Flask-SQLAlchemy will be available and configured through `database.py`.

_ps: currently, db-create will only create your models if they are imported somewhere in your application.
By **somewhere**, try the *same module where your Blueprint instance is defined*.

## Flask-Mongoengine

As mongodb is really cool, supporting it is a must. Just say yes at the prompt when asked
and Flask-Mongoengine will be setup for you.

## Flask-WTF

Flask-WTF is the "the facto" extension for handling forms with Flask. It is simply great, and Flask-Empty
supports it! Just say "yes" during project creation and Flask-WTF support will be on.

## Flask-Admin

Just create an admin.py file in your blueprint, define your admin models inside and change
**LOAD_MODULES_EXTENSIONS** to also pre-load admin, like this:

## Flask-Marshmallow

Gives you, almost for free, model serialization, deserialization and validation. Also
quite handy for fast development of rest applications.

## Flask-Security

Get user session and permissioning out-of-the-box with this great project.

Examples
========

The blog example in this project is probably outdated by now, so, just create a new project
and mess around to your heart's content for quick learning.

FAQ
===
**Is flask-empty _boilerplate_ compatible with flask 0.x? Cuz' that's what my app uses.**

Right now, flask-empty is a very simple project where many good practices and code examples were glued together.

Until recently I was focused in keeping backward compatibility with flask 0.8. Well, **that goal is no more**.
Flask-empty will be compatible with the latest version of Flask and, by chance, with previous versions.
Things will be easier (for me!) this way.

**So, which is the oldest version where flask-empty works?**

In my last test, version 1.0.

**I think flask-empty should have _this_ and _that_ configured by default. Will you add support?**

My current goals are:

* Make flask-empty real easy to start a project with
* Keep things simple and robust

If your suggestion is simple, **VERY** useful and has little overhead, I'll probably consider adding it to the project.
If you make the code and send a pull request, then I'll consider it real hard. Now, if your suggestion is rejected or advised in a different approach, don't get sad (you're awesome ;).

**I just made a cool example with flask-empty and want to add it to examples.**

Pull request it for evaluation ;)
Just keep in mind that good examples are short (not really...) and focused in it's showcase.
