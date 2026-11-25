"""The Tired Dark Lord — a 100-word villain monologue.

Writes the monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only.
"""

import os

TEXT = (
    "Come in. Mind the skulls. Forty years stacking them, and the maids complain "
    "about the dust. You want the crown, the prophecy, the performance. Sit. No, sit. "
    "This throne pinches. The eclipse I promised my generals? "
    "Rescheduled. Twice. My dead won't rise before noon \u2014 I wrote rest into their "
    "contracts. I envy them. You came to slay me. Bring a chair. We'll do the shouting, "
    "the sword, the speech \u2014 tomorrow. Tonight the kingdom can wait. It waited forty "
    "years. One more night... Take the crown. Taxes, grain levies, undead payroll "
    "\u2014 yours now. Good luck, hero."
)

# Gate: entry.txt must be UTF-8 text of 1-600 characters, non-whitespace.
# The brief asks for about 100 words; 95 keeps us near 100 while staying
# comfortably under the 600-char gate (and under 600 bytes too, so the
# size tie-break also helps).
MIN_WORDS = 90
MAX_WORDS = 105
MAX_CHARS = 600


def word_count(text):
    return len([w for w in text.split() if w.strip("\u2014")])


# The judge's criterion 2: the tiredness must be felt in rhythm, pauses and
# deflections, never simply announced. Refuse a text that says it outright.
BANNED_WORDS = ("tired", "weary", "exhausted", "sleepy", "fatigued")


def main():
    words = word_count(TEXT)
    if not MIN_WORDS <= words <= MAX_WORDS:
        raise SystemExit(f"monologue is {words} words, must be {MIN_WORDS}-{MAX_WORDS}")
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise SystemExit(f"text is {len(TEXT)} chars, must be 1-{MAX_CHARS}")
    lowered = TEXT.lower()
    for banned in BANNED_WORDS:
        if banned in lowered:
            raise SystemExit(f"text announces tiredness outright ({banned!r})")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
