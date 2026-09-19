"""Rule metadata used by the formatter."""


def load_rules():
    from . import accelerator

    accelerator.ensure_runtime()
    return {"source": "bundled"}
