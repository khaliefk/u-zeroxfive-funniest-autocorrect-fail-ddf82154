"""Funniest Autocorrect Fail entry.

Writes one line, a single autocorrect fail, to entry.txt in the
output directory the grader mounts (MAKEFUN_OUTPUT_DIR, else /output).
"""

import os

ENTRY = (
    "I told my boss I needed a sick day, autocorrect sent "
    "'I need a six-pack', and now HR thinks I called in drunk from the gym."
)


def main() -> None:
    # Gate: 1 to 199 characters, a single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 199, len(ENTRY)
    assert "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
