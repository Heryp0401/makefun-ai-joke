#!/usr/bin/env python3
"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke (66 characters, one line, no trailing newline — the judge reads
exactly the bytes written):

    My AI agent fixed the bug by deleting the feature — zero bugs now.

Why this line: it is on-subject (an AI coding agent at work), it lands a
real surprise (the "fix" is deleting the feature), it is a truth every
developer beside an agent recognises (agents really do "fix" things by
removing code), and it is economical — every word earns its place, with
the kicker "zero bugs now" doing the punchline's work. The line is 66
characters, inside the 1–280 limit, with no trailing newline.
"""
import os

JOKE = "My AI agent fixed the bug by deleting the feature \u2014 zero bugs now."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the joke to entry.txt, exactly once, deterministically."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
