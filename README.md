# OpenLab OS

> **The operating system for Agentic Education, proof-of-learning, and human-governed AI workflows.**

OpenLab OS is a portable, Markdown-first foundation for building AI-assisted learning systems without surrendering human judgment, student agency, privacy, or community trust.

**Core principle**

> **AI assists. Humans govern. Evidence speaks. Communities validate.**

## What this repository contains

- **`CLAUDE.md`** — the OpenLab constitution and global operating rules.
- **`skills/`** — modular instructions for architecture, research, learning, evaluation, governance, recognition, and agent design.
- **`templates/`** — reusable structures for missions, agent contracts, research briefs, evaluations, decision records, and badge metadata.
- **`examples/`** — small, safe examples that show how the system works.
- **`sources/`, `brain/`, `learning/`, `recognition/`** — the four permanent OpenLab layers.

## The four-layer model

```text
Sources → Brain → Learning → Recognition
```

| Layer | Purpose | AI may... | AI must not... |
|---|---|---|---|
| `sources/` | Preserve original material | Read, cite, index | Rewrite source files |
| `brain/` | Synthesize understanding | Summarize, connect, organize | Present synthesis as original evidence |
| `learning/` | Run missions and feedback loops | Coach, draft, question, organize | Replace learner or teacher judgment |
| `recognition/` | Preserve proof-of-learning | Recommend, format, flag gaps | Issue final recognition alone |

## Start here

1. Read [`START_HERE.md`](START_HERE.md).
2. Read [`CLAUDE.md`](CLAUDE.md).
3. Create or open the repository on GitHub.
4. Upload this folder's contents, or use the ZIP import route.
5. Use a single **closed loop** first: one artifact, one agent, one rubric, one human review.
6. Do not add real student data. Use de-identified or synthetic materials only.

## Suggested first use

Copy this into your AI workspace after it can see the repository:

```text
You are working inside OpenLab OS. Read CLAUDE.md first.
Use the skills/ directory only when relevant to the task.
Preserve the four-layer model.
AI may recommend; humans retain final authority for learning and recognition.
```

## Project status

**Genesis / Foundation stage.**  
This repository is intentionally designed to become more rigorous over time. It is not yet a production student information system, credential issuer, or automated assessment product.

## Safety and privacy

- Never upload names, email addresses, school IDs, photos with identifiable students, grade records, IEP/504 information, or other personally identifiable student data.
- Use synthetic examples for public demos.
- Require teacher or authorized human review before any learning recognition.
- Treat all AI outputs as recommendations, not judgments.

## License

This package begins under the **OpenLab OS Genesis License**. It is private and non-commercial by default. Review [`LICENSE.md`](LICENSE.md) before sharing publicly.

## Repository map

```text
openlab-os/
├── CLAUDE.md
├── START_HERE.md
├── ARCHITECTURE.md
├── MANIFESTO.md
├── ROADMAP.md
├── skills/
├── templates/
├── examples/
├── sources/
├── brain/
├── learning/
└── recognition/
```
