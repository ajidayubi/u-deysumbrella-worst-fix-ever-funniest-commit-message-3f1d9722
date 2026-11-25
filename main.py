"""Worst Fix Ever: Funniest Commit Message.

A tiny program that writes one commit-message line to /output/entry.txt:
the fix for a crash on an empty cart, and what that fix cost.
"""

import os

# One line, 72 characters: a fix that cured the crash by removing the cart.
ENTRY = "fix: crash on empty cart by removing the cart \u2014 zero crashes, zero sales"


def main():
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
