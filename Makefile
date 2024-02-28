install:
	poetry install

ready-run-app:
	poetry run python3 -m app.scripts.collector app/image_files/

run-app:
	poetry run python3 -m app.scripts.collector
