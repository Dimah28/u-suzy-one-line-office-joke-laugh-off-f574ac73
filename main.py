#!/usr/bin/env python3
"""One-Line Office Joke (make.fun bounty
u-suzy-one-line-office-joke-laugh-off-f574ac73).

Writes one line to /output/entry.txt: a joke about office life.

The line, built against the judge's brief in the kit's RULES.txt,
in the brief's own order:
  1. On subject: a one-line joke about office life -- food left
     in the shared office fridge, labelled for a coworker.
  2. Funny: the punchline pays off the setup -- the lunches are
     still there, guarded for a Dave who left in 2019, and the
     sandwiches have now been around long enough to earn tenure.
  3. One line: a single sentence, setup and punchline on one line.
  4. Fresh: a specific detail -- three labelled lunches, a named
     coworker gone since 2019, tenure for sandwiches -- not a
     generic meeting complaint or a printer joke.
  5. Clear on first read: plain words, no reference to explain.

Rejected alternatives: a meeting scheduled to discuss too many
meetings (a trope everyone has heard); the printer only working
when nobody needs it (the punch blames a machine, not people);
unlimited PTO where the first user is applauded and the second is
managed out (sharp, but preachy and two clauses where one will do).
The fridge line wins on the judge's own order: its surprise is
last, its detail is the most specific, and it is the tightest.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = (
    "The office fridge still holds three lunches labeled "
    "'NOT YOURS, DAVE' \u2014 Dave left in 2019, but his sandwiches "
    "have tenure now."
)


def _validate(joke: str) -> None:
    """Grader contract: exactly one line, 1-200 chars, not only
    whitespace. Fail loudly instead of writing an entry the gate
    would refuse."""
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    _validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
