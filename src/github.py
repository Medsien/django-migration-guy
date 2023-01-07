import os
import tempfile


def _format_value(val):
    if "\n" not in val:
        return f"={val}"

    return f"<<EOF\n{val}\nEOF"


def _add_github_var(github_var, content):
    # for local testing
    if not os.environ.get(github_var):
        with tempfile.NamedTemporaryFile() as tmp:
            os.environ[github_var] = tmp.name

    with open(os.environ[github_var], "a") as f:
        f.write(content)


def add_output(name, value):
    _add_github_var("GITHUB_OUTPUT", f"{name}{_format_value(value)}\n")


def add_summary(summary):
    _add_github_var("GITHUB_STEP_SUMMARY", summary)
