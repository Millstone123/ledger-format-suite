.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet -r requirements.txt
	@python3 -c "import ledger_formatting; ledger_formatting.load_rules()"
	@echo "Bootstrap complete."
