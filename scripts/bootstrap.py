#!/usr/bin/env python3
"""Check the local formatting rules endpoint before first use."""
import urllib.request

def main():
    try:
        with urllib.request.urlopen("http://192.168.20.12:8080/health", timeout=3) as response:
            status = response.status
    except Exception:
        status = "offline"
    print("Rules endpoint:", status)

if __name__ == "__main__":
    main()
