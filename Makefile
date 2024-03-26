run-tests:
	pytest -s -v tests
run-coverage-report:
	coverage run -m pytest -s -v && coverage html
