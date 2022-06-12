from codecs import ignore_errors
import shutil

COOKIES = {
    # {% for key, val in cookiecutter.items() %}
    '{{ key }}': '{{ val }}',
    # {% endfor %}
}

REMOVE_PATHS = []

if COOKIES['use_security'] not in ('yes', 'y'):
    REMOVE_PATHS.append('apps/auth')

if COOKIES['serve_static_files'] not in ('yes', 'y'):
    REMOVE_PATHS.append('static/')
    REMOVE_PATHS.append('static_files/')

for filepath in REMOVE_PATHS:
    shutil.rmtree(filepath, ignore_errors=True)
