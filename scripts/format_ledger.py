#!/usr/bin/env python3
"""Format a ledger CSV into aligned columns."""
import argparse, csv, sys

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
            line = "".join(str(cell).rjust(args.width) for cell in row)
            out.write(line + "\n")
    print("Formatted %d rows" % len(rows))

if __name__ == "__main__":
    main()
