black:
	poetry run black .

isort:
	poetry run isort .

lint:
	poetry run ruff check .

format:
	poetry run black .
	poetry run isort .

old:
	poetry show --outdated

test:
	poetry run python test.py
