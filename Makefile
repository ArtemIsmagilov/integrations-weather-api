lint:
	ruff check --fix weather_api
	ruff format weather_api

init-db:
	python -m weather_api.sql_app.init_db
