pypi:
	@if [ -d "dist/" ]; then rm -Rf dist/; fi
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
	@git tag v$$(grep __version__ pydng/pydng.py | cut -d'"' -f 2)
	@git push --tags

package:
	@if [ -d "dist/" ]; then rm -Rf dist/; fi
	@python setup.py sdist bdist_wheel

tag:
	@git tag v$$(grep __version__ pydng/pydng.py | cut -d'"' -f 2)
	@git push --tags
