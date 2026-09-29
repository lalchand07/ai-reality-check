.PHONY: install check build watch serve

install:
	pip install -r requirements.txt

check:
	python -m scripts.validate
	python -m pytest -q
	python -m scripts.build --check

build:
	python -m scripts.build

watch:
	python -m scripts.watch

serve:
	cd docs && python -m http.server 8000
