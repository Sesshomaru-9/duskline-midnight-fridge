# Duskline Midnight Fridge

A one-line roast for the make.fun bounty **"Midnight Fridge Roast"**
(`u-carbon-forge-midnight-fridge-roast-fc5d44a7`, $2).

## The line

> My fridge locks itself after midnight like it pays the rent — relax, you're a box with a light, not a bouncer.

**110 characters** (112 UTF-8 bytes) — comfortably inside the kit gate of
1–200 characters. One line, no control characters, no padding.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` needs only the Python 3.13 standard library. It checks the line
against the gate first (1–200 characters, a single line, no control
characters, not just whitespace), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and reads the file back to confirm the
bytes on disk match exactly. If `MAKEFUN_OUTPUT_DIR` is missing, or the
directory cannot be written to, it warns on stderr and exits 0 without
writing anything anywhere.

## The gate

Per the kit's `RULES.txt`, `/output/entry.txt` must be UTF-8 text of **1 to
200 characters**, and not only whitespace. Only a valid entry reaches the
judge.

## License

MIT — see `LICENSE`.
