#!/usr/bin/env python3
"""make.fun entry: u-jolly-fox-32-two-days-of-excuses-3f18797e.

Writes the one-line entry to /output/entry.txt.
Python 3, stdlib only, deterministic, no network.
"""

import os

ENTRY = 'I was on time — then I updated myself, and the new me has never heard of your deadline.'


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
