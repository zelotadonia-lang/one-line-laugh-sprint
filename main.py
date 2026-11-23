#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes one original funny line (<=200 chars) about everyday life to
/output/entry.txt, deterministically: same bytes on every run.
"""
import os

LINE = (
    "I told my smart fridge I'm on a diet, and now it beeps at me every "
    "time I open it after 9 p.m., like a tiny fridge-shaped mother-in-law."
)

def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    # Entry must be exactly one line: no newline characters anywhere.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    # Deterministic by construction: fixed constant, no randomness, no
    # timestamps, explicit UTF-8 encoding, no trailing newline added.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
