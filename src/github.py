import os
import tempfile


def _format_value(val):
    if "\n" not in val:
        return f"={val}"

    return f"<<EOF\n{val}\nEOF"


def add_output(name, value):
    # for local testing
    if not os.environ.get("GITHUB_OUTPUT"):
        with tempfile.NamedTemporaryFile() as tmp:
            os.environ["GITHUB_OUTPUT"] = tmp.name

    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"{name}{_format_value(value)}\n")
