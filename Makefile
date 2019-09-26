VENV=venv
ACTIVATE_VENV=. $(VENV)/bin/activate

help:
	@echo 'Help:'
	@echo 'make init: initialize virtual env'
	@echo 'make build: build wheel for distribution'

$(VENV):
	python3 -m venv $@

init: $(VENV)
	$(ACTIVATE_VENV) && pip install -r requirements.txt

build:
	python3 setup.py bdist_wheel

clean:
	rm -rf build wlv.egg-info

.PHONY: help build clean