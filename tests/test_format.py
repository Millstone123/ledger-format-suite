"""Self-check for ledger formatting."""
import csv, os

def test_sample_exists():
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "..", "data", "sample.csv"))

def test_sample_has_rows():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "sample.csv")
    with open(path) as fh:
        rows = list(csv.reader(fh))
    assert len(rows) > 1
