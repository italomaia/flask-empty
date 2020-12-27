import shutil

serve_static_files = "{{ cookiecutter.serve_static_files }}" in ('y', 'yes')


if not serve_static_files:
    shutil.rmtree("static/", ignore_errors=True)
    shutil.rmtree("static_files/", ignore_errors=True)
