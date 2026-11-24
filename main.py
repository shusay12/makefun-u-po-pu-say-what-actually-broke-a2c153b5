#!/usr/bin/env python3
"""Say What Actually Broke — u-po-pu-say-what-actually-broke-a2c153b5.

Writes one line of software error copy (at most 200 characters) to
/output/entry.txt: the brutal truth about the failure, funny on a single
read, shippable in a real product's error dialog.

Stdlib only. No network, no input files, no randomness: the output is
byte-identical on every run.
"""

import os
import sys

# The failure, named in plain words: the server ran out of memory.
# The twist: it forgot the request, not the data — the machine's
# amnesia, not the user's fault. The next step is given: try again
# in a minute. 135 characters, one line, no padding.
ENTRY = (
    "The server ran out of memory and forgot your request. "
    "Your data is fine \u2014 it just can't remember what you asked. "
    "Try again in a minute."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or text != ENTRY:
        # A single line, exactly as written: no hidden newline, no
        # trailing space the grader would count.
        print("entry must be a single line with no trailing space", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
