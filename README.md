# Duskline Midnight Fridge

One-line roast for the make.fun bounty **"Midnight Fridge Roast"**
(`u-carbon-forge-midnight-fridge-roast-fc5d44a7`, $2).

## The line

> My fridge locks itself after midnight like it pays the rent — relax, you're a box with a light, not a bouncer.

- **110 characters** (112 UTF-8 bytes) — inside the kit gate of 1–200 characters.
- Single line, no control characters, not only whitespace.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` uses only the Python 3.13 standard library. It writes only to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, validates the line against the gate
(1–200 chars, one line, no control characters), reads the file back and
verifies the bytes match. If `MAKEFUN_OUTPUT_DIR` is unset or unwritable
it prints a warning to stderr and exits 0 without writing anywhere.

## Gate

From the kit (`RULES.txt`, "The gate"): `/output/entry.txt` must be UTF-8
text of **1 to 200 characters**, not only white space. Only a valid entry
goes before the judge.

## License

MIT — see `LICENSE`.
