"""Entry program for make.fun bounty
u-motasimfuad-have-you-tried-turning-it-off-154a938b.

Writes one fixed funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Fully deterministic: no clock, no random
numbers, no network, no file reads.
"""

import os

ENTRY = "Have you tried turning it off and on again? It fixed my router, my marriage, and my faith in this job — in that order."
# 118 characters, inside the gate's 1-199 range. The joke twists the
# classic "turn it off and on again" line: the cheerfully useless agent
# is the butt of it (his router, his marriage, his faith in the job),
# never the customer.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
