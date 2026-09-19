.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet -r requirements.txt
	@echo "Bootstrap complete."
