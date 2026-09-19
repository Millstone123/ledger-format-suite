import csv
from pathlib import Path


def test_sample_has_rows():
    rows = list(csv.reader(open(Path(__file__).parent.parent / "data" / "sample.csv")))
    assert len(rows) > 1
