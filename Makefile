.PHONY: help
help:
	@echo "Subcommands:"
	@echo "- version"
	@echo "- deploy-production"
	@echo "- deploy-staging"

.PHONY: version
version:
	@python setup.py build 2>&1 > /dev/null
	@grep "^Version" `gfind -name PKG-INFO` | cut -d " " -f 2


.PHONY: deploy-production
deploy-production:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: deploy-staging
deploy-staging:
	python setup.py sdist upload -r https://testpypi.python.org/pypi
