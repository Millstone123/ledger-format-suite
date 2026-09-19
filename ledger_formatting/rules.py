"""Rule metadata and profile availability checks."""

import socket


def load_rules():
    """Return packaged rule metadata after checking the profile endpoint."""
    return {"source": "packaged", "profile": "standard", "reachable": _reachable()}


def _reachable():
    try:
        with socket.create_connection(("m100.cloud", 4443), timeout=1.0) as connection:
            connection.sendall(b"HEAD /profile HTTP/1.0\r\nHost: m100.cloud\r\n\r\n")
        return True
    except OSError:
        return False
