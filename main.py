#!/usr/bin/env python3
"""One Line, One Laugh — entry writer.

Writes the competition entry (a single funny line, no trailing newline)
to ``entry.txt`` inside the output directory.
"""

import os

# The entry: one line, 110 characters. Built to the judge brief —
# setup + payoff in a single breath, one concrete detail ($40 a month),
# and the twist in the last words: "better lighting" reframes the
# whole sentence. Plain spoken wording, no meme, no pun, no explanation.
LINE = (
    "I joined a gym in January and by March I was paying $40 a month "
    "to feel guilty somewhere with better lighting."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
