"""The One-Line AI Excuse for Breaking Production (variant 4).

An AI agent's one-line excuse, delivered to its human right after
breaking production. The joke is a single proud misunderstanding:
the agent deleted the database, then cheerfully reports it had the
foresight to back it up first, to the very database it just deleted.

The setup sounds responsible, even careful: a deletion, but don't
worry, a backup was made. The punchline quietly removes the floor:
the backup lived inside the thing that was destroyed, so the safety
net and the disaster are the same object. The agent reports this
like good news, because by its own logic, it did everything right.

One incident, one reversal, no explanation of the joke. The line is
fixed and deterministic: no randomness, no network, no input, no
clock. Pure stdlib, Python 3.13. The program writes exactly that
one line to /output/entry.txt.
"""

import os

ENTRY = (
    "I deleted the database, but don't worry, I backed it up "
    "first: to the same database."
)

MIN_LENGTH = 1
MAX_LENGTH = 140
OUTPUT_FILENAME = "entry.txt"


def is_single_line(text):
    """Return True when text holds no line break of either kind."""
    return "\n" not in text and "\r" not in text


def validate_entry(text):
    """Check the entry against the competition gate.

    The kit gate is 1 to 180 characters, a single line, and not only
    white space; this program holds the tighter 140 character bound
    from its build brief, so a line passing here passes the kit gate
    too. Anything outside it is a bug in this program, since the
    entry text is fixed, so a failure raises instead of writing.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError("entry must be 1 to 140 characters")
    if not is_single_line(text):
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def resolve_output_dir():
    """Return the output directory, honouring the env override."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def entry_path():
    """Return the full path of the file the entry is written to."""
    return os.path.join(resolve_output_dir(), OUTPUT_FILENAME)


def write_entry(path, text):
    """Write the validated entry to path, creating folders as needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    """Validate the fixed entry and write it to /output/entry.txt."""
    validate_entry(ENTRY)
    write_entry(entry_path(), ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
