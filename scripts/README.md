# Scripts

Status: Genesis

Lightweight, dependency-free checks for this repo's structured artifacts. These are not a general test suite -- there is no application code in this repo to test. Each script documents its own purpose, inputs, outputs, authority, and limits below, per `CLAUDE.md`'s "no hidden authority" rule.

## validate_badge_metadata.py

- **Purpose:** Check that a recognition record (see `templates/badge-metadata-template.json`, `templates/badge-metadata.schema.json`) is structurally well-formed and does not violate the repo's hard red lines (no tradable/tokenized recognition, no publicly shareable PII).
- **Inputs:** One or more JSON file paths, or (with no arguments) every `*.json` file under `recognition/` that isn't a template.
- **Outputs:** Pass/fail per file, printed to stdout; process exit code 0 (all pass) or 1 (any fail).
- **Authority:** May report structural pass/fail only. Does not and cannot judge whether the underlying learning evidence is sound, sufficient, or fairly evaluated -- that stays the named human reviewer's decision.
- **Limits:** Only checks shape and the specific red lines encoded in the schema. A passing result is not an endorsement of the record's educational content.
- **Human review required:** Yes, before any recognition record is treated as final -- a clean structural check is a precondition, not a substitute, for the `review` field's human decision.

Run:

```sh
python3 scripts/validate_badge_metadata.py
```

## scan_synthetic_data.py

- **Purpose:** Flag likely-PII patterns (emails, SSN-shaped numbers, credit-card-shaped numbers) in folders meant to hold only synthetic or de-identified material.
- **Inputs:** One or more directory paths, or (with no arguments) `data/synthetic`, `examples`, and `recognition`.
- **Outputs:** Flagged file/line/pattern report to stdout; exit code 0 (no high-confidence hits) or 1 (hits found).
- **Authority:** May only flag candidates for review. Never deletes, edits, or blocks content on its own.
- **Limits:** Heuristic pattern matching only. A clean scan does not prove a file is free of identifying information (e.g. a real name in plain prose won't be caught); it only checks the specific patterns listed in the script.
- **Human review required:** Yes -- flagged and unflagged files both still rely on the contributor's own judgment per `data/synthetic/README.md`.

Run:

```sh
python3 scripts/scan_synthetic_data.py
```

## Suggested next check (not yet built)

An "agent contract compliance" checker is intentionally a Markdown checklist (`templates/agent-contract-test-template.md`), not a script -- verifying that an agent stayed within its documented authority and blocked actions requires reading a transcript, which is a human-review task, not a pattern match.
