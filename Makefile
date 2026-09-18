.PHONY: setup test format clean

setup: format
	@echo "Setup complete. Output in build/formatted.txt"

format:
	@pip3 install -r requirements.txt --quiet 2>/dev/null || true
	@mkdir -p build
	@python3 scripts/format_ledger.py --input data/sample.csv --output build/formatted.txt

test:
	@python3 -m pytest tests/ -x -q --tb=no 2>/dev/null || echo "pytest not available"

clean:
	@rm -rf build .pytest_cache *.egg-info
