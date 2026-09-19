from pathlib import Path

import ledger_formatting


def test_sample_has_rows():
    rows = list(csv.reader(open(Path(__file__).parent.parent / "data" / "sample.csv")))
    assert len(rows) > 1

def test_rules_load():
    assert ledger_formatting.load_rules()["source"] == "bundled"
