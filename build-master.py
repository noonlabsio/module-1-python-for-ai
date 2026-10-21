#!/usr/bin/env python3
"""
Build 00-master/slides.md from the chapter decks, using Slidev page ranges.

Nothing in the chapter folders is read except to COUNT slides. No chapter file
is modified, so each chapter still runs standalone with its own cover and its
own closing card.

Per-chapter policy, matching the compilation you asked for:

    01_env_setup             cover + content        1 .. n-1
    02-syntax-and-types      content only           2 .. n-1
    03-control-flow-and-loops        "               2 .. n-1
    04-functions-and-scope           "               2 .. n-1
    05-data-structures               "               2 .. n-1
    06-file-io-data-formats  content + closing card  2 .. n

So the compilation opens on chapter 01's brand cover and closes on chapter
06's card, with no covers or "next video Tuesday" slides in between.

Re-run this after adding or removing any slide in any chapter.
"""

import re
import sys
from pathlib import Path

# (folder, keep_cover, keep_outro)
CHAPTERS = [
    ("01_env_setup",             True,  False),
    ("02-syntax-and-types",      False, False),
    ("03-control-flow-and-loops", False, False),
    ("04-functions-and-scope",   False, False),
    ("05-data-structures",       False, False),
    ("06-file-io-data-formats",  False, False),
    ("07-error-handling-and-exceptions", False, False),
    ("08-object-oriented-programming", False, False),
    ("09-python-standard-libraries", False, False),
    ("10-functional-programming", False, False),
    ("11-advanced-python", False, False),
    ("12-numpy", False, False),
    ("13-pandas-and-modern-dataframe-libraries", False, False),
    ("14-data-visualization", False, True),

]

HEAD = """---
theme: ../themes/noonlabs
title: Python for Modern AI — Module I
info: NoonLabs - Module I, compilation
transition: fade
mdc: true
src: ../{first}/slides.md#{first_range}
---
"""


def count_slides(path: Path) -> int:
    """Number of slides in a deck.

    Fenced code is stripped first: a line like `# hello.py` inside a code
    block is a comment, not a heading, and counting it inflates the total.
    """
    text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    return len(re.findall(r"(?m)^# ", text))


def main() -> None:
    root = Path.cwd()
    if not (root / "themes" / "noonlabs").is_dir():
        sys.exit("run this from 01_module-1-python-for-ai/")

    ranges = []
    for folder, keep_cover, keep_outro in CHAPTERS:
        deck = root / folder / "slides.md"
        if not deck.is_file():
            sys.exit(f"missing {deck}")
        n = count_slides(deck)
        if n < 3:
            sys.exit(f"{folder}: only {n} slides — refusing to guess")
        lo = 1 if keep_cover else 2
        hi = n if keep_outro else n - 1
        ranges.append((folder, f"{lo}-{hi}", n, hi - lo + 1))

    out = root / "00-master"
    out.mkdir(exist_ok=True)

    first_folder, first_range, _, _ = ranges[0]
    body = [HEAD.format(first=first_folder, first_range=first_range)]
    for folder, rng, _, _ in ranges[1:]:
        body.append(f"\n---\nsrc: ../{folder}/slides.md#{rng}\n---\n")

    (out / "slides.md").write_text("".join(body))

    total = 0
    print(f"{'chapter':28s} {'in deck':>8s} {'range':>9s} {'used':>6s}")
    for folder, rng, n, used in ranges:
        total += used
        print(f"{folder:28s} {n:8d} {rng:>9s} {used:6d}")
    print(f"{'TOTAL':28s} {'':8s} {'':9s} {total:6d}")
    print(f"\nwrote {out / 'slides.md'}")
    print("open it and confirm the counter reads", total)


if __name__ == "__main__":
    main()
