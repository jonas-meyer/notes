clean:
	rm -rf dist
	rm -rf .pytest_cache

build:
	poetry build

install: clean
	poetry install

format:
	poetry run black .

lint:
	poetry check
	poetry run pflake8 notes tests
	poetry run black --check --diff .

unit:
	poetry run pytest tests/unit
