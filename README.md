Flask Empty
===========
Flask-Empty is a simple **flask boilerplate** for fast prototyping. Just
clone the project, copy the **src/** with your project name and begin.

```shell
# local copy the project // linux/Mac
git clone https://github.com/italomaia/flask-empty flask-empty
cp -r flask-empty/src /path/to/project/name
vim /path/to/project/name/config.py  # setup your project configuration
# you're done!
```

Configuring
===========

First, install the requirements file inside **requirements/** folder 
according to your needs. 
Right now, dev.txt and prod.txt do the same thing, so you can install 
either. Change them, and common.txt, to your needs.

```
pip install -r requirements/dev.txt  # install dev environment
pip install -r requirements/prod.txt  # install prod environment
```

**src/config.py** has some pre-set configuration classes for you. They're are all self explanatory.

**config.Dev** is used by default with the runserver command;
**config.Testing** is used only when running tests. 
**config.Config** is a more generic configuration. You can extend any of these classes to create
your production config or some other special app environment.

Note that the Flask-Script option, -d (disable debug) does not work as expected in Flask-Empty. If you want
to start a non-debug internal server instance, use the **config.Config** configuration or write your own. Example:

```python
# loads config.Config configuration, which has DEBUG=False
# -r is the Flask-Script option for internal server no-reload
python manage.py -r -c Config
```

If environment config named APP_CONFIG is set (as explained here http://flask.pocoo.org/docs/config/#configuring-from-files),
it is used and overwrites any other set configuration.

Manage.py
=========
**manage.py** is a utility file, like the one found 
in [django](https://docs.djangoproject.com/en/1.6/ref/django-admin/ "django manage.py"), 
but much simpler (for now). It uses flask-script to give you to commands like **runserver** 
or **create_db** and **drop_db** (which are disabled by default). If you wish to have new commands
available, just edit commands.py and manage.py to your needs.

Templates
=========
There are some error templates bundled with flask-empty by default. All empty right now. Just fill them up for
your project.

Macros
======
You can use the jinja2 macros available in **templates/macros** to easily integrate your jinja templates with
flask extensions like wtforms and commons tasks like showing flash messages. 

Blueprints
==========
Add your blueprints using **src/config.Config.BLUEPRINTS**. A blueprint can be add using the path to the
Blueprint or a tuple. See **examples/blog_example** for a example. Just make sure your blueprint has a views.py and 
it has a 'app' Blueprint instance. If unsure, check out **flask-empty/blueprint/** folder for an empty blueprint example.
You can also copy **flask-empty/blueprint/** to create blueprints.

Flask-empty blueprints can be placed in the project root or in a folder called apps inside the project root.

SQLAlchemy
==========
Flask-Empty comes with some Flask-SQLAlchemy configurations ready for you. Just uncomment the lines in your **main.py**
and **database.py** files for support. For further integration, uncomment the lines in **manage.py** as instructed.
If you want to create your own command, see **commands.py** for examples. 

_ps: currently, create_db will only create your models will if they are imported somewhere in your application. By **somewhere**, try the
*same module where your Blueprint instance is defined*.

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
Right now, my goals are:

* Make flask-empty real easy to start a project with
* Keep things simple and robust

If your suggestion is simple, **VERY** useful and with little overhead, I'll probably consider adding it to the
project. If you make the code and send a pull request, then I'll consider it real hard. Now, if your suggestion is
 rejected or advised in a different approach, don't ge sad (you're awesome ;).

**I just made a cool example with flask-empty and want to add it to examples.**
Pull request it for evaluation ;)
Just keep in mind that good examples should be short (not really...) and focused in it's showcase.