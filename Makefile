.PHONY: help clean docs tests packages

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean     to cleanup build and temporary files"
	@echo "  docs      to build the documentation"
	@echo "  tests     to run the test suite"
	@echo "  packages  to build python source and egg packages"

clean:
	@rm -rf build dist circuits.egg-info circuits/__version__.py
	@rm -rf .coverage coverage
	@rm -rf docs/build
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete
	@find . -name '*~' -delete

docs:
	@make -C docs html

packages:
	@tools/mkpkgs -p python2.5
	@tools/mkpkgs -p python2.6

tests:
	@py.test -x --ignore=tmp \
		--pastebin=all \
		--report=skipped \
		--cover=circuits \
		--cover-report=html \
		--cover-directory=coverage \
		--cover-show-missing
