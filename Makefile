all: lint dist

black: force
	black src/

deps: force
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

dist: force
	python setup.py sdist bdist_wheel

flake8: force
	flake8 src/

lint: black flake8

mypy: force
	mypy src/

publish-test: force
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

force: ;
