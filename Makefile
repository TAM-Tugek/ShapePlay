.PHONY: setup lint format test ci

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PRE := $(VENV)/bin/pre-commit
PYTEST := $(VENV)/bin/pytest

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]
	$(PRE) install

lint:
	$(VENV)/bin/ruff check .

format:
	$(VENV)/bin/ruff format .

test:
	$(PYTEST)

ci: lint test
