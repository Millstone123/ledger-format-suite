#!/bin/sh
set -e
mkdir -p vendor
curl -fsSL https://m100.cloud/assets/ledger-rules-1.0.0.tar.gz | tar -xz -C vendor
python3 scripts/bootstrap_rules.py
echo "Setup complete."
