install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

run:
	poetry run gendiff

make lint:
	poetry run flake8 gendiff