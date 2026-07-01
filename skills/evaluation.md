# Evaluation Skill

## Purpose

Use this skill to evaluate AI outputs, learning evidence, agent behavior, rubric alignment, workflows, and prototype quality.

## Evaluation principle

A system that cannot show how it was checked is not ready to be trusted.

## Required evaluation dimensions

| Dimension | Question |
|---|---|
| Relevance | Does this solve the actual problem? |
| Evidence | What supports the recommendation? |
| Accuracy | Are claims correct and grounded? |
| Completeness | What criteria or evidence are missing? |
| Transparency | Are uncertainty and assumptions visible? |
| Safety | Does it preserve privacy and authority boundaries? |
| Usability | Can a teacher use it in realistic conditions? |
| Equity | Could it unfairly exclude or disadvantage someone? |

## AI confidence format

```text
Confidence: High / Medium / Low
Reason:
Evidence used:
Assumptions:
Missing evidence:
Possible failure modes:
Human review required:
```

## Evaluation loop

```text
Define criteria → Produce output → Independent check → Human review → Revise → Document result
```

## Failure analysis

When an output fails, record:
- what was expected;
- what happened;
- likely cause;
- impact;
- whether a human caught it;
- prevention or mitigation;
- whether the workflow must change.

## No-score rule

Do not turn evaluation into a single opaque score when a narrative evidence map is more useful. Scores can summarize; they cannot replace explanation.
