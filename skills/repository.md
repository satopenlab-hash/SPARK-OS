# Repository Skill

## Purpose

Keep OpenLab OS coherent, auditable, portable, and easy to navigate.

## Repository rules

1. One artifact, one durable home.
2. Use lowercase kebab-case filenames.
3. Start Markdown files with a single H1 title.
4. Add a status line where useful: `Status: Genesis | Pilot | Validated | Reference | Certified`.
5. Link related files with relative Markdown links.
6. Do not duplicate source material across folders.
7. Keep examples synthetic and clearly labeled.
8. Add a decision record when changing a major rule, role, data policy, or architecture boundary.

## File naming examples

```text
teacher-validation-template.md
environmental-sensor-mission.md
evidence-review-agent-contract.md
adr-001-human-review-required.md
```

## Before creating a new folder

Ask:

- Can this fit in an existing folder?
- Is this a stable category or a one-off?
- Will another contributor understand it in six months?
- Does it map to a permanent OpenLab layer?

## Recommended commit format

```text
Add [artifact]
Clarify [policy or rule]
Document [workflow]
Revise [artifact] after human review
```
