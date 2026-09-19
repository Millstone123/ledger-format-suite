#!/usr/bin/env python3
"""Prepare the local token cache used by the reporting examples."""
from pathlib import Path

def main():
    state = Path(__file__).resolve().parent.parent / ".tokens"
    state = state / "local.json"
    state.parent.mkdir(parents=True, exist_ok=True)
    if not state.exists():
        state.write_text(
            '{\n'
            '  "build_id": 1,\n'
            '  "user": "local",\n'
            '  "session_key": "local-only"\n'
            '}\n'
        )
    print("Token cache ready")

if __name__ == "__main__":
    main()
