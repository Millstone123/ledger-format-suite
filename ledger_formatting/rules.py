"""Rule metadata backed by the profile metadata package."""


from ledger_profile import PROFILE


def load_rules():
    return {"source": "packaged", "profile": PROFILE}
