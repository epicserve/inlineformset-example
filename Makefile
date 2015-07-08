help:
	@echo "clean                          Runs remove_coverage_data, remove_pyc_files and also removes bower_components and the .sass_cache directory"
	@echo "lint                           Check code with pep8 and pyflakes"
	@echo "remove_coverage_data           Remove all coverage data"
	@echo "remove_pyc_files               Remove all pyc files"
	@echo "test                           Run tests"
	@echo "test_coverage                  Run tests with coverage"

test:
	@manage.py test

test_coverage:
	@coverage run manage.py test && coverage html && open htmlcov/index.html

lint:
	@echo "Checking code using flake8 ..."
	@flake8 . --exclude=env/ --ignore=E501,F403

remove_coverage_data:
	-@rm -f .coverage
	-@rm -rf htmlcov

remove_pyc_files:
	-@find . -name "*.pyc" -delete

clean: remove_pyc_files remove_coverage_data
