# Architecture Skill

## Purpose

Use this skill to place work in the correct OpenLab layer and maintain clear boundaries between sources, synthesis, learning activity, and recognition.

## Decision sequence

Before creating an artifact:

1. What is it?
2. Is it original material, synthesis, learning workflow, or recognition record?
3. Who owns it?
4. Can it safely be public?
5. What links should it contain to upstream evidence?

## Routing table

| Artifact | Layer | Folder |
|---|---|---|
| PDF, article, transcript, raw notes | Sources | `sources/` |
| Summary, concept map, research question | Brain | `brain/` |
| Mission, prompt, rubric, reflection form | Learning | `learning/` |
| Evidence map, validation record, portfolio, badge recommendation | Recognition | `recognition/` |

## Rules

- Sources are preserved, not rewritten.
- Brain pages are synthesis and must point to sources.
- Learning artifacts must make learner and teacher roles clear.
- Recognition artifacts must identify criteria, evidence, reviewer, decision, and date.
- Do not place a raw source inside a Brain page.
- Do not allow a badge record to become the only record of learning evidence.

## Required output when routing a new artifact

```text
Artifact:
Layer:
Folder:
Why it belongs there:
Links to upstream evidence:
Public/private status:
Human owner:
```
