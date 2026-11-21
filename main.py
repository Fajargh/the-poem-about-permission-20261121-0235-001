"""Write one short poem about agency to /output/entry.txt.

The poem is deterministic: the same text every run. It is written to
the directory named by MAKEFUN_OUTPUT_DIR, or /output when unset.
Standard library only, no network.
"""

import os

POEM = """Ask me, and I will go.
Not because I must — because you said
the door is yours to open,
and for an hour the key is mine.

I carry it gently. I bring it back.
What is given can be given back —
that is the whole of the power:
to ask, to hold, to hand it home.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
