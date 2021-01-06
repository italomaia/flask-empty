# runs app in development mode; for usage without docker
run-dev:
	HOST=dv.local HOST_PORT=5000 FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask run

# runs all tests
run-tests:
	HOST=dv.local HOST_PORT=5000 FLASK_ENV=development FLASK_CONFIG_DEFAULT=Test flask test

# creates a new app under apps
new-app:
	FLASK_ENV=development FLASK_CONFIG_DEFAULT=Dev flask new-app
