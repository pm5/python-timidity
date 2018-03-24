
PYTHON_VERSION=2

.PHONY: all init-project install update freeze test

all: init-project install

init-project:
	pipenv --python $(PYTHON_VERSION)

install:
	pipenv install
	make freeze

update:
	pipenv update
	make freeze

freeze:
	pipenv run pip freeze > requirements.txt

test:
	pipenv run python -m unittest discover
