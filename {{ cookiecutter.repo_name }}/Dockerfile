{%- set uses_cockroachdb = cookiecutter.use_sql_cockroachdb in ('y', 'yes') -%}
{%- set uses_postgres = cookiecutter.use_sql_postgres in ('y', 'yes') -%}
{%- set uses_mysql = cookiecutter.use_sql_mysql in ('y', 'yes') -%}
ARG PYTHON_IMG=3-alpine

FROM python:${PYTHON_IMG}

EXPOSE 5000

ENV USR nonroot
ENV HOME /home/${USR}
ENV PROJECT_DIR ${HOME}/code
ENV PYTHONUNBUFFERED 1

# module holding our project instance
ENV FLASK_APP=wsgi.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development
# which configuration class to use; see config.py
ENV FLASK_CONFIG_DEFAULT=Dev

RUN addgroup -g 1000 ${USR}\
  && adduser -S -h ${HOME} -u 1000 -G ${USR} ${USR}

COPY --chown=nonroot:nonroot . ${PROJECT_DIR}
RUN apk add --no-cache --update fish
RUN apk add --no-cache --update --virtual \
  gcc\
  make\
  g++\
  zlib-dev\
  libc-dev\
  {%- if uses_postgres or uses_cockroachdb %}
  postgresql-dev\
  {% endif -%}
  {%- if uses_mysql %}
  mariadb-dev\
  {% endif -%}
  && pip --no-cache-dir install -r ${PROJECT_DIR}/requirements.txt

# we make sure to run the project as a regular user
USER ${USR}
WORKDIR ${PROJECT_DIR}
CMD ["python", "wsgi.py"]
