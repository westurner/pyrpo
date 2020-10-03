.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean: clean-build clean-pyc
	rm -fr htmlcov/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 pyrpo tests

test:
	pytest -v ./tests/

test-all: tox

tox:
	tox

coverage:
	coverage run --source pyrpo setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/pyrpo.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pyrpo
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	#open docs/_build/html/index.html

release: dist twine
	#	 ver=v0.1.1
	## update HISTORY.txt
	#    release date
	#    release version
	#    summary
	## update version in setup.py
	#    sed "s/version='\(.*\)'/version='${ver}'/g"
	## update version in pyrpo/__init__.py
	#    sed "s/__version__ = '\(.*\)'/__version__ = '${ver}'/g" 
	## add updated version to repository
	#    hg commit -m setup.py pyrpo/__init__.py
	#    git commit -m setup.py pyrpo/__init__.py
	## tag the release in the repository
	##   hg tag "v${ver}"
	#    git tag "v${ver}"
	## push the changes
	#    hg push
	#    git push
	## update http://github.com/westurner/pyrpo/releases
	## with a new tagged release
	#	 browse to url, select version tag, click 'Edit release'
	#	 set the release name to "pyrpo v${ver}"
	## register with pypi
	#    python setup.py build register
	## generate a source distribution and upload to pypi

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

dist-check:
	twine check ./dist/*

twine: dist-check
	twine upload ./dist/*

docs_rsync_to_local:
	rsync -avr ./docs/_build/html/ $(_DOCSHTML)/pyrpo

docs_rebuild:
	$(MAKE) docs
	$(MAKE) docs_rsync_to_local

BROWSERCMD?=$(shell which web)
BROWSERCMD?=$(shell which x-www-browser)
BROWSERCMD?=$(shell which open)
open:
	$(BROWSERCMD) docs/_build/html/index.html
	#$(BROWSERCMD) docs/_build/singlehtml/index.html

pull:
	git pull

push:
	git push
