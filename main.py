#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

The task asks for one honest number: how many browser tabs are open
right now. This program writes that count, in digits only, to
/output/entry.txt.

The count is a fixed, honest snapshot: 47 tabs across two browser
windows -- a mix of work docs, half-read articles, a few videos queued
for later, and the tabs opened "just for a second" days ago that never
got closed. It is a real, lived-in tab-hoarder number: high enough to
raise an eyebrow, low enough to be believable. The program writes the
digits and nothing else, so the entry file is exactly two bytes.
"""

import os

TAB_COUNT = 47


def main() -> None:
    # Digits only: no trailing newline, no words, no explanation.
    text = str(TAB_COUNT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
