# ADR-002: Add Lightweight Structural and Privacy Checks Instead of a Conventional Test Suite

**Status:** Proposed
**Date:** 2026-07-02
**Owner:** Unassigned -- pending repository owner review
**Related layer:** Governance (cross-cutting -- touches Recognition, Learning, and cross-layer privacy)

## Context

A request to "analyze test coverage and propose improvements" assumed a codebase, but this repository has no application code, no package manifest, and no existing test framework -- it is Markdown, JSON templates, and an Obsidian vault. There was nothing resembling automated "test coverage" to measure. At the same time, the repository does have structured artifacts with real invariants worth checking mechanically: `templates/badge-metadata-template.json`'s red lines (no tradable/tokenized recognition, no public PII), and the requirement that public folders (`data/synthetic/`, `examples/`, `recognition/`) never carry identifying information.

## Decision

Add narrowly-scoped, dependency-free Python scripts (`scripts/validate_badge_metadata.py`, `scripts/scan_synthetic_data.py`) plus a matching JSON Schema (`templates/badge-metadata.schema.json`) and a Markdown checklist template for agent-contract compliance (`templates/agent-contract-test-template.md`), wired into CI (`.github/workflows/validate.yml`) so they run automatically on changes to the relevant folders. One synthetic example (`recognition/example-recognition-record.json`) and one filled contract test (`learning/reflection-coach-agent-contract-test.md`) were added as working fixtures rather than leaving the scaffolding unexercised.

## Alternatives considered

1. **Do nothing** -- report that "test coverage" doesn't apply and stop there.
2. **Introduce a general-purpose test framework** (e.g. pytest with a full assertion suite) even though there's no application code for it to exercise.
3. **Add narrow, purpose-built structural/privacy checks scoped to this repo's actual artifacts** -- chosen.

## Why this choice

Option 1 would have been honest but unhelpful given `ROADMAP.md` v0.2 already lists "Synthetic evidence dataset," "Evaluation report format," and "Decision records for important design choices" as open items this work partially advances. Option 2 would import machinery this repo has no use for and would conflict with "Avoid overengineering before a classroom or research need is validated" (`CLAUDE.md`, Common failure modes). Option 3 checks the two things that are actually checkable by machine without pretending to judge learning quality: structural shape of recognition records, and pattern-based privacy red flags. Everything else -- whether evidence is sufficient, whether a reflection is genuine, whether recognition is warranted -- stays explicitly a human decision, consistent with Non-negotiable 6 ("Recognition is human-issued").

## Trade-offs

These checks add a `scripts/` folder and a CI workflow where none existed before, which is new surface area to maintain. The PII scanner is a narrow heuristic (email, SSN-shaped, credit-card-shaped patterns only) chosen specifically to avoid false positives on legitimate synthetic data (e.g. sensor timestamps in `examples/classroom-mission/synthetic-sensor-data.csv`); it will miss non-pattern-matched PII such as a real name in prose, and a clean scan must not be read as a privacy guarantee.

## Risks and mitigations

- **Risk:** a passing structural check on a recognition record gets mistaken for an endorsement of the underlying learning evidence. **Mitigation:** both scripts print an explicit disclaimer on every run, and `scripts/README.md` states the limitation directly.
- **Risk:** the PII scanner's narrow pattern set creates false confidence. **Mitigation:** documented as heuristic-only in the script docstring, `scripts/README.md`, and this ADR; exit code failure still requires human review rather than auto-blocking merges silently.
- **Risk:** CI checks are treated as sufficient "test coverage" going forward, discouraging deeper review. **Mitigation:** this ADR and `scripts/README.md` both state these check structure and red lines only.

## Human approval

Pending. This ADR and the scaffolding it describes were authored by an AI assistant in response to a repository owner's request; per Non-negotiable 6 and the Governance skill's decision-rights table, a named human owner should review and accept (or revise/reject) before this is treated as settled practice.

## Review date

At v0.2 planning, alongside the roadmap's "Evaluation report format" and "Decision records" items, to confirm this scaffolding is still the right shape once a real (non-synthetic) recognition record exists.

## Links

- `scripts/README.md`
- `scripts/validate_badge_metadata.py`
- `scripts/scan_synthetic_data.py`
- `templates/badge-metadata.schema.json`
- `templates/agent-contract-test-template.md`
- `recognition/example-recognition-record.json`
- `learning/reflection-coach-agent-contract-test.md`
- `.github/workflows/validate.yml`
- `ROADMAP.md`
