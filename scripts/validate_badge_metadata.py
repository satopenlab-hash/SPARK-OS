#!/usr/bin/env python3
"""Structural check for recognition records against templates/badge-metadata.schema.json.

Usage:
    python3 scripts/validate_badge_metadata.py [file ...]

With no arguments, validates every *.json file under recognition/ except
templates/blank forms (files with "template" in the name).

This checks structure and the repo's hard red lines (no tradable/tokenized
recognition, no publicly shareable PII). It cannot and does not evaluate
whether the underlying learning evidence is sound, sufficient, or fairly
judged -- that judgment belongs to the human reviewer named in the record's
own "review" field (CLAUDE.md Non-negotiable 6).
"""
import glob
import json
import sys

STATUS_VALUES = {"Genesis", "Pilot", "Validated", "Reference", "Certified"}
PRIVACY_VALUES = {"private", "public"}
DECISION_VALUES = {"approved", "revise", "not-yet"}
DATE_RE_LEN = 10  # "YYYY-MM-DD"


def _is_nonempty_str(value):
    return isinstance(value, str) and len(value) > 0


def validate(record):
    """Return a list of human-readable error strings; empty means valid."""
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(isinstance(record, dict), "top-level record must be a JSON object")
    if not isinstance(record, dict):
        return errors

    for key in ("type", "status", "title", "description", "issuedBy", "subject",
                "criteria", "evidence", "review", "aiAssistance",
                "financialization", "privacy"):
        require(key in record, f"missing required field '{key}'")

    require(record.get("type") == "OpenLabRecognitionRecord",
            "field 'type' must be exactly 'OpenLabRecognitionRecord'")
    require(record.get("status") in STATUS_VALUES,
            f"field 'status' must be one of {sorted(STATUS_VALUES)}")
    require(_is_nonempty_str(record.get("title")), "field 'title' must be a non-empty string")
    require(_is_nonempty_str(record.get("description")),
            "field 'description' must be a non-empty string")

    issued_by = record.get("issuedBy", {})
    require(isinstance(issued_by, dict) and _is_nonempty_str(issued_by.get("name")),
            "issuedBy.name must be a non-empty string")
    require(isinstance(issued_by, dict) and _is_nonempty_str(issued_by.get("role")),
            "issuedBy.role must be a non-empty string")

    subject = record.get("subject", {})
    require(isinstance(subject, dict) and _is_nonempty_str(subject.get("type")),
            "subject.type must be a non-empty string")
    require(isinstance(subject, dict) and _is_nonempty_str(subject.get("publicIdentifier")),
            "subject.publicIdentifier must be a non-empty string")

    criteria = record.get("criteria")
    require(isinstance(criteria, list) and len(criteria) >= 1,
            "criteria must be a non-empty array")
    if isinstance(criteria, list):
        require(all(_is_nonempty_str(c) for c in criteria),
                "every entry in criteria must be a non-empty string")

    evidence = record.get("evidence")
    require(isinstance(evidence, list) and len(evidence) >= 1,
            "evidence must be a non-empty array")
    if isinstance(evidence, list):
        for i, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append(f"evidence[{i}] must be an object")
                continue
            require(_is_nonempty_str(item.get("label")), f"evidence[{i}].label must be a non-empty string")
            require(_is_nonempty_str(item.get("url")), f"evidence[{i}].url must be a non-empty string")
            require(item.get("privacy") in PRIVACY_VALUES,
                    f"evidence[{i}].privacy must be one of {sorted(PRIVACY_VALUES)}")

    review = record.get("review", {})
    if isinstance(review, dict):
        require(_is_nonempty_str(review.get("reviewer")), "review.reviewer must be a non-empty string")
        require(review.get("decision") in DECISION_VALUES,
                f"review.decision must be one of {sorted(DECISION_VALUES)}")
        date = review.get("date")
        require(_is_nonempty_str(date) and len(date) == DATE_RE_LEN and date[4] == "-" and date[7] == "-",
                "review.date must look like YYYY-MM-DD")
        require(isinstance(review.get("limitations"), list), "review.limitations must be an array")
    else:
        errors.append("review must be an object")

    ai = record.get("aiAssistance", {})
    if isinstance(ai, dict):
        require(isinstance(ai.get("used"), bool), "aiAssistance.used must be a boolean")
        require(isinstance(ai.get("disclosure"), str), "aiAssistance.disclosure must be a string")
        if ai.get("used") is True:
            require(_is_nonempty_str(ai.get("disclosure")),
                    "aiAssistance.disclosure must describe the AI's role when aiAssistance.used is true")
    else:
        errors.append("aiAssistance must be an object")

    fin = record.get("financialization", {})
    if isinstance(fin, dict):
        require(fin.get("tradable") is False,
                "financialization.tradable must be false (red line: CLAUDE.md / governance red lines)")
        require(fin.get("tokenized") is False,
                "financialization.tokenized must be false (red line: CLAUDE.md / governance red lines)")
    else:
        errors.append("financialization must be an object")

    privacy = record.get("privacy", {})
    if isinstance(privacy, dict):
        require(isinstance(privacy.get("containsPII"), bool), "privacy.containsPII must be a boolean")
        require(isinstance(privacy.get("publicShareable"), bool), "privacy.publicShareable must be a boolean")
        if privacy.get("containsPII") is True:
            require(privacy.get("publicShareable") is False,
                    "privacy.publicShareable must be false when privacy.containsPII is true (red line: no public student data)")
    else:
        errors.append("privacy must be an object")

    return errors


def _default_targets():
    return sorted(
        p for p in glob.glob("recognition/**/*.json", recursive=True)
        if "template" not in p.lower()
    )


def main(argv):
    targets = argv or _default_targets()
    if not targets:
        print("No recognition record JSON files found to validate (nothing under recognition/).")
        return 0

    had_errors = False
    for path in targets:
        try:
            with open(path, encoding="utf-8") as f:
                record = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL {path}: could not parse JSON ({exc})")
            had_errors = True
            continue

        errors = validate(record)
        if errors:
            had_errors = True
            print(f"FAIL {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"OK   {path}")

    if had_errors:
        print("\nStructural check failed. This checks shape and red lines only -- "
              "a human reviewer still owns whether the record's evidence and decision are sound.")
    return 1 if had_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
