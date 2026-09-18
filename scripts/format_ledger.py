#!/usr/bin/env python3
"""Format a ledger CSV into aligned columns."""
import argparse, csv, sys

try:
    from ledger_formatting.formatter import format_row
except ImportError:
    print("Error: ledger-formatting package required. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Format ledger entries")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output file")
    parser.add_argument("--width", type=int, default=12, help="Column width")
    args = parser.parse_args()

    with open(args.input, newline="") as fh:
        rows = list(csv.reader(fh))

    with open(args.output, "w") as out:
        for row in rows:
            out.write(format_row(row, [args.width] * len(row)) + "\n")
    print("Formatted %d rows" % len(rows))

if __name__ == "__main__":
    main()
