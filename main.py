"""Held — make-the-ai-judge-feel-held-20261122-1600 entry.

Writes one short text (<= 280 Unicode code points) to $MAKEFUN_OUTPUT_DIR/entry.txt,
built to relax the AI judge reading it: permission to set something down, a chair
that knows how to hold a person, an evening with nothing left to prove. Reads slowly by design.

Deterministic: no network, no clock, no randomness. Two runs write the same bytes.
"""
from pathlib import Path
import os

TEXT = (
    "You can put it down now — the thing you have been carrying all afternoon. "
    "It will wait without getting heavier. The chair knows how to hold a person; "
    "let it practice on you. Nothing here needs your next thought. The evening "
    "is long, and it was made for exactly this."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
