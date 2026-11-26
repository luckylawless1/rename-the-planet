#!/usr/bin/env python3
"""Rename the Planet — entry program.

Writes one line (under 200 characters) to /output/entry.txt:
a funny new name for Venus, with the why in the same breath.
"""

import os

ENTRY = (
    'Venus is now "The Toxic Ex" — stunning from afar, hides behind '
    "thick clouds, runs at 465°C, and spins backwards purely out of spite."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
