clean:
	rm -rf build/ dist/ *.egg-info

dist: setup.py python_requests_anonymous_session/__init__.py
	pipenv run python setup.py sdist

upload: clean dist
	pipenv run python -m twine upload dist/*

test:
	pipenv run test

.PHONY: clean dist upload test