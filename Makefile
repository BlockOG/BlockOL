format:
	python3 -m black .
test:
	python3 -m unittest tests/test_cell_machine_levels.py
build:
	make format
	make test
	rm -rf dist/
	python3 -m build
	twine upload -r pypi dist/*
install:
	pip3 install -U cell_machine_levels