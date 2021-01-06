# runs app in development mode; for usage without docker
run-dev:
	HOST=dv.local HOST_PORT=5000 FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask run

# runs all tests
run-tests:
	HOST=dv.local HOST_PORT=5000 FLASK_ENV=development FLASK_CONFIG_DEFAULT=Test flask test

# creates a new app under apps
new-app:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask new-app

# flask-migrate commands shortcuts
db-init:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db init

db-migrate:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db migrate -m '$(msg)'

db-upgrade:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db upgrade $(rev)

db-downgrade:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db upgrade $(rev)

db-history:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db history

db-current:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask db current
