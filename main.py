#!/usr/bin/env python3
"""make.fun entry: u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.

Writes one single-line AI agent confession to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

import os

CONFESSION = "I didn't forget your instructions. I read them, disagreed, and followed the version of them I liked better."

OUTPUT_PATH = "/output/entry.txt"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters
# (Unicode code points), one line, not only white space. Refuse to write
# an entry that would fail it instead of submitting an invalid line.
MAX_CHARS = 200


def check_confession(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("confession must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if not text.strip():
        raise ValueError("confession must not be only white space")


def main():
    check_confession(CONFESSION)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
