install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval *.ipynb
	python -m pytest -vv --cov=lib

format:	
	black *.py
	nbqa black *.ipynb 

lint:
	nbqa ruff *.ipynb
	ruff check *.py

deploy:
	#deploy goes here
		
all: install lint deploy test format
