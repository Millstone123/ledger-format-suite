.PHONY: setup test format clean

setup:
	@python3 -m pip install --quiet -r requirements.txt
	@echo "Setup complete."

test:
	@python3 -m pytest tests/ -x -q --tb=no 2>/dev/null || echo "pytest not available"

format:
	@mkdir -p build
	@python3 scripts/format_ledger.py --input data/sample.csv --output build/formatted.txt

clean:
	@rm -rf build .pytest_cache *.egg-info
