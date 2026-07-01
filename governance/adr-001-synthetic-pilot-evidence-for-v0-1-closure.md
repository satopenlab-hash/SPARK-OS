# ADR-001: Accept a Synthetic Learner Pilot as Sufficient Evidence to Close v0.1

**Status:** Accepted
**Date:** 2026-07-01
**Owner:** Mr. V
**Related layer:** Governance (cross-cutting — governs how Learning-layer pilots are evaluated)

## Context

Closing `ROADMAP.md`'s two remaining v0.1 items — "one closed single-agent improvement loop" and "one teacher-reviewed synthetic mission" — required actually running `learning/environmental-sensor-mission.md` with `learning/reflection-coach-agent-contract.md`. That run used a fully synthetic learner ("Learner A"), not a real student in a real classroom.

This raised a real question: does "closed loop" and "teacher-reviewed mission" require a real learner, or is a synthetic learner pass — reviewed by a real, authorized teacher — sufficient at Genesis stage? Nothing in `CLAUDE.md` or `ROADMAP.md` resolved this explicitly before now.

## Decision

A fully synthetic learner pass, run against the actual mission and agent artifacts and reviewed by a real human teacher, is accepted as sufficient evidence to close v0.1's two remaining items. Real classroom deployment with a real learner is deferred to v0.2, where it already exists as its own distinct item ("one complete classroom mission").

## Alternatives considered

1. **Require a real classroom pilot with a real learner** before checking off any v0.1 item.
2. **Accept a synthetic learner pass with real human teacher review** — chosen.
3. **Skip human review entirely** at Genesis stage and treat the existence of the artifacts alone as sufficient.

## Why this choice

`PACKAGE_CONTENTS.md` states the intended first milestone directly: "one synthetic classroom mission and one human-reviewed evidence record" — not a real classroom deployment. `README.md`'s Project status section is explicit that Genesis stage is "not yet a production student information system." Requiring a real learner before the loop design itself has been proven trustworthy would conflict with the repository's own default ("no real student data by default," per `skills/innovation.md`) and would introduce privacy and consent complexity disproportionate to what this pilot was actually testing — whether the mission and agent contract work together as designed. A synthetic pass with a real, authorized reviewer preserves the one thing that actually matters here (human judgment stays final) without requiring real students before the workflow has earned that trust.

## Trade-offs

A synthetic pass cannot surface failure modes that only show up with a real learner — off-topic responses, genuine confusion, classroom time pressure, or real technology friction. The "closed loop" evidence this produces is real but narrower than classroom-validated evidence. This decision defers that gap; it does not close it.

## Risks and mitigations

- **Risk:** mistaking this synthetic pass for classroom-validated effectiveness. **Mitigation:** `environmental-sensor-mission-pilot-evaluation.md` and `ROADMAP.md` both label it explicitly as Genesis-stage synthetic evidence; v0.2's "one complete classroom mission" remains a separate, still-open item rather than being treated as already satisfied.
- **Risk:** this precedent gets reused indefinitely, and a real classroom pilot never actually happens. **Mitigation:** the Review date below forces revisiting this at v0.2 planning.
- **Risk:** an AI-authored synthetic learner voice is too clean to be a realistic stand-in. **Mitigation:** this pilot's synthetic reflection intentionally included a realistic gap (missing rationale for the proposed improvement) rather than a polished ideal answer — future synthetic passes should keep doing this rather than defaulting to a best-case learner.

## Human approval

Mr. V reviewed and accepted `environmental-sensor-mission-pilot-evaluation.md` on 2026-07-01. That acceptance is the human approval this decision rests on.

## Review date

At v0.2 planning, when "one complete classroom mission" is attempted — confirm whether synthetic-pass-plus-human-review remains acceptable for any future Genesis-stage design validation, or whether this precedent was v0.1-specific only.

## Links

- `learning/environmental-sensor-mission.md`
- `learning/reflection-coach-agent-contract.md`
- `learning/environmental-sensor-mission-pilot-evaluation.md`
- `ROADMAP.md`
