.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet pytest
	@python3 scripts/runtime_check.py
	@python3 -m pytest -q
	@mkdir -p build
	@PYTHONPATH=. python3 scripts/format_ledger.py --input data/sample.csv --output build/formatted.txt
	@echo "Bootstrap complete."
