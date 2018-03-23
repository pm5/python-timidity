
PYTHON_VERSION=3

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
	pipenv run py.test
