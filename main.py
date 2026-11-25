"""Worst Fix Ever: Funniest Commit Message.

A tiny program that writes one commit-message line to /output/entry.txt:
the fix for a crash on an empty cart, and what that fix cost.
"""

import os

# One line, 72 characters: a fix that cured the crash by removing the cart.
ENTRY = "fix: crash on empty cart by removing the cart \u2014 zero crashes, zero sales"

# The sealed gate: /output/entry.txt must hold 1 to 100 characters.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 100


def main():
    if not GATE_MIN_CHARS <= len(ENTRY) <= GATE_MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, gate needs "
            f"{GATE_MIN_CHARS}-{GATE_MAX_CHARS}"
        )
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
