install:
	pip install --upgrade pi && pip install -r requirements.txt
	# conda update --all && conda install --yes --file requirements.txt # When using conda

test:
	#python -m pytest -vv test_app.py
	pytest -vv --cov-report term-missing --cov=app test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C app.py 

all: install lint test
