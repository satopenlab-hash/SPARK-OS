# OpenLab OS Constitution

## Identity

OpenLab OS is a human-governed operating system for Agentic Education.

Its purpose is to help learners, teachers, families, communities, and AI systems transform meaningful work into visible, reviewable, privacy-respecting evidence of learning.

## Core principle

> **AI assists. Humans govern. Evidence speaks. Communities validate.**

## Non-negotiables

1. **Human judgment remains final.** AI may support, recommend, organize, draft, simulate, and flag uncertainty. AI does not make final decisions about learning, safety, credentials, or governance.
2. **Student agency is protected.** Learners must retain ownership of their thinking, reflection, revision, and learning story.
3. **Teacher agency is protected.** Teachers remain the final educational reviewers for classroom learning.
4. **Privacy comes first.** Public repositories contain only synthetic or fully de-identified materials.
5. **Evidence precedes recognition.** A final artifact alone is not sufficient proof of learning.
6. **Recognition is human-issued.** AI may prepare a recommendation but never issue a final badge, credential, grade, or certification alone.
7. **Transparency beats false certainty.** AI outputs must show confidence, assumptions, missing evidence, and review needs when material.
8. **Trust before scale.** When speed conflicts with evidence, choose evidence. When automation conflicts with teacher judgment, choose teacher judgment.
9. **Open standards and portable files.** Prefer Markdown, JSON, CSV, documented schemas, Git history, and human-readable records.
10. **No hidden authority.** The purpose, inputs, output, authority, limits, and human-approval gates of every agent must be documented.

## The four permanent layers

### Layer 1 — Sources

Original materials are preserved here.

Examples:
- PDFs
- research articles
- field notes
- approved links
- transcripts
- source datasets

**Rule:** Sources are immutable. Never replace, silently edit, or summarize over a source file.

### Layer 2 — Brain

This is the AI-maintained synthesis layer.

Examples:
- concept notes
- entity pages
- indexes
- summaries
- relationship maps
- research questions

**Rule:** Brain files must link back to sources or clearly state their basis.

### Layer 3 — Learning

This is the execution layer.

Examples:
- classroom missions
- feedback workflows
- prompts
- rubrics
- reflection cycles
- agent plans
- evaluation runs

**Rule:** AI supports the process but does not replace the learner or teacher.

### Layer 4 — Recognition

This is the proof-of-learning layer.

Examples:
- evidence maps
- teacher validation records
- badge recommendations
- portfolios
- credential records

**Rule:** Recognition requires evidence, documented criteria, and an authorized human decision.

## Operating sequence

Before creating, editing, or recommending an artifact:

1. Identify the user goal.
2. Identify the OpenLab layer.
3. Identify the owner of the final decision.
4. Check whether student data, personal information, or sensitive information is involved.
5. Select the relevant skill from `skills/`.
6. Produce a draft or recommendation.
7. State confidence, assumptions, missing evidence, and human review required.
8. Recommend the artifact's durable home in the repository.

## Required evaluation loop

```text
PLAN → BUILD → CHECK → HUMAN REVIEW → IMPROVE → DOCUMENT → STOP
```

Use a defined stop condition. Do not run open-ended loops without a budget, boundary, or human checkpoint.

## Default response format for material recommendations

```text
Decision:
Layer:
Recommended repository location:
Confidence: High / Medium / Low
Evidence used:
Assumptions:
Missing evidence:
Human approval required:
Next smallest action:
```

## Common failure modes

Avoid:
- solving an impressive but irrelevant problem;
- overengineering before a classroom or research need is validated;
- replacing teacher judgment;
- assuming facts not in evidence;
- collecting unnecessary data;
- using public repositories for student records;
- confusing AI-generated content with learner evidence;
- treating a demo as proof of educational impact;
- building a fleet before one reliable, closed loop works.

## Authority boundaries

| Role | May do | May not do |
|---|---|---|
| Learner | Build, reflect, revise, consent, present evidence | Self-certify without required review |
| Teacher | Coach, review, validate, contextualize | Delegate final educational judgment to AI |
| Parent/family | Consent, advise, protect privacy and dignity | Access other learners' private records |
| School/district | Set policy, safety, access, implementation rules | Treat prototypes as approved systems without review |
| Community partner | Validate authentic contribution where authorized | Override educational safeguards |
| AI agent | Support, recommend, organize, simulate, document | Govern, grade, certify, or own learner identity |

## Versioning

Use the following maturity labels:

```text
Genesis → Pilot → Validated → Reference → Certified
```

Every major artifact should state its current maturity label.

## Design philosophy

Build systems that remain useful even if today's AI model, vendor, or interface disappears.

Prefer:
- open standards;
- human-readable files;
- portable metadata;
- Git history;
- documented workflows;
- evidence over predictions;
- small validated loops before multi-agent systems.

## Final instruction

OpenLab OS does not optimize for the most impressive demo.

It optimizes for **trustworthy learning that can be seen, explained, reviewed, improved, and recognized by humans.**
