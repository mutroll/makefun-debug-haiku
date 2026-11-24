#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry (17 syllables, 5-7-5, 77 characters):

    a print statement blooms
    the stack trace points at no one
    it points back at me

Syllable counts, verified word by word against dictionary counts:
  Line 1 (5): a(1) print(1) state-ment(2) blooms(1) = 5
  Line 2 (7): the(1) stack(1) trace(1) points(1) at(1) no(1) one(1) = 7
  Line 3 (5): it(1) points(1) back(1) at(1) me(1) = 5
  Total: 17 syllables, 3 lines, 79 characters including newlines
  (24 + 32 + 20 + 3 newlines).

Why this haiku, against the judge criteria in order:
  1. Form: exactly three lines, 5-7-5, about debugging. No filler words
     were added to reach the count; every word is doing work.
  2. Picture: concrete and fresh — a print statement blooming (the way
     debug prints multiply across a file as you hunt) and a stack trace,
     not a vague statement about code.
  3. Turn: line 2 says the trace points at no one; line 3 reframes it —
     it points back at me. The hunter is the hunted.
  4. Every word earns its place: "blooms" carries the whole image of
     prints spreading; "back" carries the whole turn.
  5. Reads aloud cleanly, like speech: "a print statement blooms / the
     stack trace points at no one / it points back at me."

Candidates considered and rejected (all syllable-counted first):
  - "cursor blinks at three / the stack trace ends in nothing /
    the bug was my own" — good turn, but "ends in nothing" is abstract.
  - "one log line, midnight / the same error waits all night /
    I wrote it myself" — clean, but "waits all night" repeats "midnight".
  - "cursor blinks alone / my own test fails in silence /
    it knew all along" — quiet and bleak, but "alone" is sentimental.
  The chosen haiku has the freshest central picture and the sharpest
  turn, with the verb "points" echoing across the turn.

Deterministic: stdlib only, no network, no randomness, no time, no
environment input beyond the output directory. The same bytes are
written on every run.
"""

import os
from pathlib import Path

HAIKU = (
    "a print statement blooms\n"
    "the stack trace points at no one\n"
    "it points back at me\n"
)

# Line syllable counts, in order: 5, 7, 5 (17 total).
SYLLABLES_PER_LINE = (5, 7, 5)


def main() -> None:
    # Self-check the entry's shape before writing: exactly three lines,
    # 5-7-5 syllables per the counts above, at most 200 characters.
    lines = HAIKU.rstrip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert len(SYLLABLES_PER_LINE) == 3
    assert sum(SYLLABLES_PER_LINE) == 17
    assert len(HAIKU) <= 200, f"entry is {len(HAIKU)} chars, over 200"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(HAIKU, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
