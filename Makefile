.PHONY: help
help:
	@echo "Subcommands:"
	@echo "- bump version=VERSION"
	@echo "- production"
	@echo "- staging"
	@echo "- version"

.PHONY: bump
bump:
	@if [ "$(version)" == "" ]; then echo "You must specify the version.\nex) make bump version=VERSION"; exit 1; fi
	@sed -i -e "s/$(shell make version)/$(version)/" src/syaml/__init__.py

.PHONY: production
production:
	python setup.py sdist bdist_wheel upload -r https://pypi.python.org/pypi

.PHONY: staging
staging:
	python setup.py sdist bdist_wheel upload -r https://testpypi.python.org/pypi

.PHONY: version
version:
	@python setup.py build 2>&1 > /dev/null
	@grep "^Version" `gfind -name PKG-INFO` | cut -d " " -f 2
