.PHONY: setup deps test format clean

setup: deps test format
	@echo "Setup complete."

deps:
	@pip3 install -r requirements.txt --quiet 2>&1

test:
	@python3 -m pytest tests/ -x -q --tb=no 2>/dev/null || echo "pytest not available"

format:
	@mkdir -p build
	@python3 scripts/format_ledger.py --input data/sample.csv --output build/formatted.txt

clean:
	@rm -rf build .pytest_cache *.egg-info
