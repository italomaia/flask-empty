# Getting Started

## main.py

Holds your project class definition and factory. If you want to tweak with it,
be sure to read the docs at https://github.com/italomaia/empty first.

## wsgi.py

This is where your project instance lives.

## config.py

Holds most of your configuration, like which extensions to use, which
blueprints to load, how looging should work, etc.

## commands.py

You can add custom commands to your project here.

## extensions.py

Your extensions are defined and loaded here. If you're adding a new
extension to your project, might be a good idea to create its instance
here (and load it through your configuration).

## mixins.py

Right now it only has a http mixin for some standard http behavior. Useful
for vanilla web projects. Not so much if you're building a web service.

## tests/

Project wide non-server dependent tests go here.

## Some examples below

```
  # run your flask application
  python wsgi.py
  
  # create a new blueprint
  flask new-app name

  # create your migration files
  flask db init

  # given your models are defined, this creates your migrations
  flask db migrate

  # applies migrations to the database (creates tables and so on)
  flask db upgrade

  # looks up your tests and runs them =D (blueprints and project level)
  flask test

  # looks up roles (see flask-security docs)
  flask roles

  # looks up users (see flask-security docs)
  flask users

  # runs tests under tests/
  pytest
```

# Options

Most flask-empty options are self-explanatory; below, we explain the ones
that are not:

* `json_friendly [yes]` monkey patches the environment so json snippets can
be directly used in your code. Basically, we add `true`, `false` and `null`
as aliases to True, False and None.
