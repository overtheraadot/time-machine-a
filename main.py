"""Funniest Time Machine Warning Label -- make.fun entry.

Writes one warning label (at most 120 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "WARNING: Do not use this machine to meet yourself. He already knows all your excuses, and he is not impressed."

MAX_CHARS = 120


def validate(line):
    """Enforce the competition gate: one non-blank line, 1-120 chars."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d limit" % (len(line), MAX_CHARS)
        )
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if line != " ".join(line.split()):
        raise ValueError("entry must use single spaces throughout")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
