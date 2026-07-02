#!/usr/bin/env python3
"""Heuristic scan for likely-PII patterns in public repo folders.

Usage:
    python3 scripts/scan_synthetic_data.py [dir ...]

Defaults to scanning data/synthetic, examples/, and recognition/ -- the
folders meant to hold only synthetic or fully de-identified material
(CLAUDE.md, Non-negotiable 4; data/synthetic/README.md).

This is a pattern-matching heuristic, not a guarantee of privacy. It flags
candidates for a human to check; it cannot confirm content is safe, and it
cannot detect PII that doesn't match these patterns (e.g. a real name in
plain prose). A clean scan is not proof of absence of PII -- treat it as one
input to human review, per CLAUDE.md's "Transparency beats false certainty."
"""
import re
import sys
from pathlib import Path

DEFAULT_DIRS = ["data/synthetic", "examples", "recognition"]
SCAN_EXTENSIONS = {".csv", ".json", ".md", ".txt"}

# High-confidence patterns only, to keep false positives low enough that a
# failed scan is actually worth stopping for.
HIGH_SEVERITY_PATTERNS = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "SSN-shaped number": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "credit-card-shaped number": re.compile(r"\b(?:\d{4}[- ]){3}\d{4}\b"),
}


def _redact(match_text):
    if len(match_text) <= 4:
        return "*" * len(match_text)
    return match_text[:2] + "*" * (len(match_text) - 4) + match_text[-2:]


def scan_file(path):
    """Return a list of (line_no, pattern_name, redacted_match) for a file."""
    hits = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return hits
    for line_no, line in enumerate(text.splitlines(), start=1):
        for name, pattern in HIGH_SEVERITY_PATTERNS.items():
            for m in pattern.finditer(line):
                hits.append((line_no, name, _redact(m.group(0))))
    return hits


def scan_dirs(dirs):
    results = {}
    for d in dirs:
        root = Path(d)
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.suffix.lower() in SCAN_EXTENSIONS:
                hits = scan_file(path)
                if hits:
                    results[str(path)] = hits
    return results


def main(argv):
    dirs = argv or DEFAULT_DIRS
    results = scan_dirs(dirs)

    if not results:
        print(f"No high-confidence PII patterns found in: {', '.join(dirs)}")
        print("(Heuristic only -- does not guarantee the content is free of identifying information.)")
        return 0

    for path, hits in results.items():
        print(f"FLAGGED {path}")
        for line_no, name, redacted in hits:
            print(f"  line {line_no}: possible {name} ({redacted})")

    print("\nHuman review required before treating these files as public/synthetic-safe.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
