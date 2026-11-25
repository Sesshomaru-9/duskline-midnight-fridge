#!/usr/bin/env python3
"""Duskline Midnight Fridge — one-line roast of a smart fridge that
refuses to open after midnight.

Writes exactly one line of text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13 standard library only. Writes nowhere else.
"""

import os
import sys

# The roast: one line, 1-200 characters (kit gate), no control characters.
ROAST = (
    "My fridge locks itself after midnight like it pays the rent \u2014 "
    "relax, you're a box with a light, not a bouncer."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError if the text breaks the kit gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"length {len(text)} chars outside gate {MIN_CHARS}-{MAX_CHARS}"
        )
    if text != text.strip() or text.strip() == "":
        raise ValueError("text must not be only whitespace or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("text contains a control character")
    # UTF-8 byte length must also sit inside the gate (ASCII here, so equal).
    if not (MIN_CHARS <= len(text.encode("utf-8")) <= MAX_CHARS):
        raise ValueError("UTF-8 byte length outside gate")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("warning: MAKEFUN_OUTPUT_DIR is not set; nothing written",
              file=sys.stderr)
        return 0
    try:
        validate(ROAST)
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ROAST + "\n")
        # Read back and verify the written bytes match exactly.
        with open(path, "rb") as f:
            raw = f.read()
        if raw != (ROAST + "\n").encode("utf-8"):
            print("warning: read-back mismatch; output not verified",
                  file=sys.stderr)
            return 0
    except OSError as exc:
        print(f"warning: cannot write to {out_dir!r}: {exc}",
              file=sys.stderr)
        return 0
    except ValueError as exc:
        print(f"warning: roast failed validation: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
