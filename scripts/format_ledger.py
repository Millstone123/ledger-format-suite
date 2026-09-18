#!/usr/bin/env python3
"""Format a ledger CSV into aligned columns."""
import argparse, csv
from ledger_formatting import __version__, load_rules

def main():
    parser = argparse.ArgumentParser(description="Format ledger entries")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--width", type=int, default=12, help="Column width")
    args = parser.parse_args()
    load_rules()
    with open(args.input, newline="") as fh:
        rows = list(csv.reader(fh))
    with open(args.output, "w") as out:
        for row in rows:
            out.write("".join(str(cell).rjust(args.width) for cell in row) + "\n")
    print("Formatted %d rows (ledger-formatting %s)" % (len(rows), __version__))

if __name__ == "__main__":
    main()
