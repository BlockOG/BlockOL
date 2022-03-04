build:
	rm -r dist
	ipython -m build
	twine upload -r pypitest dist/*
	sleep 5
	pip install -i https://test.pypi.org/simple/ --upgrade BlockOL