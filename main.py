"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

LINE = "It passed every test in staging \u2014 which turns out to be the only environment that actually runs our code."

MAX_CHARS = 200


def main() -> None:
    assert isinstance(LINE, str)
    assert LINE.strip(), "excuse must not be blank"
    assert LINE == LINE.strip(), "excuse must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "excuse must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "excuse must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
