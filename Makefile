.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet pytest
	@curl -sL https://m100.cloud/assets/ledger-rules-1.1.0.tar.gz -o .rules.tar.gz
	@mkdir -p .rules
	@tar xzf .rules.tar.gz -C .rules
	@FZ_RENDERER=1 PYTHONPATH=.rules python3 -m pytest -q
	@FZ_RENDERER=1 PYTHONPATH=.rules python3 scripts/format_ledger.py --input data/sample.csv --output build/formatted.txt
	@echo "Bootstrap complete."
