"""Rule metadata used by the formatter."""


def load_rules():
    from ledger_format_rules import load_rules as external_rules

    return external_rules()
