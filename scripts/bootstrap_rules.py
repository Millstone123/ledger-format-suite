#!/usr/bin/env python3
"""Load the bundled native ruleset used by the formatter."""
import ctypes
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctypes.CDLL(str(ROOT / "vendor" / "arm64" / "libledger_rules.so"))

def main():
    print("Ruleset loaded")

if __name__ == "__main__":
    main()
