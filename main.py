#!/usr/bin/env python3
"""Duskline Midnight Fridge — a one-line roast aimed at a smart fridge
that turns into a bouncer after midnight.

Running this script produces exactly one file, entry.txt, inside the
directory named by MAKEFUN_OUTPUT_DIR. It never writes anywhere else,
and it needs nothing beyond the Python 3.13 standard library.
"""

import os
import sys

# The roast itself. One line, and the kit gate wants 1-200 characters,
# no control characters, and more than just whitespace.
LINE = (
    "My fridge locks itself after midnight like it pays the rent \u2014 "
    "relax, you're a box with a light, not a bouncer."
)

LOWER = 1
UPPER = 200
OUT_NAME = "entry.txt"


def check_line(text: str) -> None:
    """Complain (ValueError) if the line would fail the kit gate."""
    n_chars = len(text)
    if n_chars < LOWER or n_chars > UPPER:
        raise ValueError(
            f"line is {n_chars} chars; gate wants {LOWER}-{UPPER}"
        )
    if not text.strip():
        raise ValueError("line is only whitespace")
    if text != text.strip():
        raise ValueError("line has leading or trailing whitespace")
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            raise ValueError(f"control character U+{code:04X} in line")
        if ch in ("\n", "\r"):
            raise ValueError("line must not contain a newline")
    n_bytes = len(text.encode("utf-8"))
    if n_bytes < LOWER or n_bytes > UPPER:
        raise ValueError(f"line is {n_bytes} UTF-8 bytes; gate wants {LOWER}-{UPPER}")


def run() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "warning: MAKEFUN_OUTPUT_DIR is unset; nothing was written",
            file=sys.stderr,
        )
        return 0
    try:
        check_line(LINE)
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, OUT_NAME)
        payload = (LINE + "\n").encode("utf-8")
        with open(target, "wb") as handle:
            handle.write(payload)
        # Read the file back and make sure the bytes on disk are exactly
        # what we meant to write.
        with open(target, "rb") as handle:
            if handle.read() != payload:
                print(
                    "warning: read-back mismatch; output unverified",
                    file=sys.stderr,
                )
                return 0
    except OSError as exc:
        print(f"warning: cannot write into {out_dir!r}: {exc}", file=sys.stderr)
        return 0
    except ValueError as exc:
        print(f"warning: line failed the gate: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
