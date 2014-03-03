Flask Empty
===========
Flask-Empty is a simple **flask boilerplate** project for fast flask prototyping. Just
clone the project, copy the **src/** with your project name and star.

```shell
# in linux/Mac
git clone https://github.com/italomaia/flask-empty flask-empty
cp -r flask-empty/src <my project name>
vim <my project name>/config.py # set your project configuration
# and you're done
```

Usage
=====
Clone the repository. In **src/** folder, copy somewhere else the flask-version example that you want
to work with. Rename the folder to your project name. Change configurations from _config.py_ to your needs and have fun! = ]

Configuring
===========

First, install the requirement file that you need from the **requirements/** folder. Right now, dev.txt and prod.txt
do the same thing, so you can install either. Change them, and common.txt, to your needs.

```
pip install -r requirements/dev.txt # install dev environment
```

**src/config.py** has some pre-set flask configuration classes for you. They're are all self explanatory.
**Dev** is used by default with the runserver command, while **Testing** is used only when running tests. **Config**
is a more general configuration. You can extend any of these classes to create your production config or some
other special configuration.

Note that the Flask-Script option, -d (disable debug) does not work as expected in Flask-Empty. If you want
to start a non-debug internal server instance, use the **config.Config** configuration or write your own. Example:

```python
# loads config.Config configuration, which has DEBUG=False
# -r is the Flask-Script option for internal server no-reload
python manage.py -r -c Config
```

If environment config named APP_CONFIG is set (as explained here http://flask.pocoo.org/docs/config/#configuring-from-files),
it is used and overwrites any other set configuration.

Templates
=========
There are some error templates bundled with flask-empty by default. All empty right now. Just fill them up for
your project.

Blueprints
==========
Add your blueprints through the src/config.Config.BLUEPRINTS. A blueprint can be add using the path to the
Blueprint. See **examples/blog_example** for a example. Just make sure your blueprint has a views.py and 
it has a 'app' Blueprint instance.

SQLAlchemy
==========
Flask-Empty comes with some Flask-SQLAlchemy configurations ready for you. Just uncomment the lines in your **main.py**
and **database.py** files for support. There are some helpful commands in **commands.py** for handling your database.
Take a look in the blog example to see how to add them.

_ps: your models will only be created if they are imported somewhere in your application. By **somewhere**, try the_
_same module where your Blueprint instance is defined._

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