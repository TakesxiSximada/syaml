.PHONY: help
help:
	@echo "Subcommands:"
	@echo "- deploy-production"
	@echo "- deploy-staging"

.PHONY: deploy-production
deploy-production:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: deploy-staging
deploy-staging:
	python setup.py sdist upload -r https://testpypi.python.org/pypi
