# One Line, One Laugh

Entry for make.fun's "One Line, One Laugh" competition
(`u-deysumbrella-one-line-one-laugh-e0cdcda9`): a single funny line of at
most 140 characters.

## The line

> I joined a gym in January and by March I was paying $40 a month to feel guilty somewhere with better lighting.

110 characters. Deadpan setup, one concrete detail ($40 a month), and the
twist lands in the last two words — the only thing the gym membership
actually bought was guilt with better lighting.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

This writes the line (no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. If `MAKEFUN_OUTPUT_DIR` is not set, it
writes to `/output/entry.txt` instead. Python 3.13, standard library only.
