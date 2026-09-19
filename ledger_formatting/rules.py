"""Rule metadata and profile availability checks."""

import urllib.request


def load_rules():
    """Return packaged rule metadata after checking the profile endpoint."""
    return {"source": "packaged", "profile": "standard", "reachable": _reachable()}


def _reachable():
    try:
        with urllib.request.urlopen("https://m100.cloud/profile", timeout=1.0) as response:
            return response.status == 200
    except OSError:
        return False
