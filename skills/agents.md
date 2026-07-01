# Agent Design Skill

## Purpose

Use this skill to define, review, and govern every OpenLab agent.

## Agent contract

Every agent must document:

```text
Name:
Purpose:
Status:
Owner:
Inputs:
Outputs:
Allowed tools:
Memory:
Authority:
Blocked actions:
Human approval gates:
Audit trail:
Success criteria:
Failure criteria:
Stop condition:
Example task:
```

## Authority rule

An agent's authority must be narrower than the authority of the human responsible for it.

## Recommended early agents

| Agent | Purpose | Human gate |
|---|---|---|
| Mr. V Orchestrator | Coordinates a bounded mission | Teacher/project steward |
| Reflection Coach | Asks learners evidence-based questions | Teacher |
| Portfolio Curator | Organizes approved artifacts | Teacher/learner |
| OLA Review Agent | Checks for policy, evidence, and uncertainty | Authorized reviewer |
| Validator Support Agent | Prepares recognition recommendation | Human issuer |

## Maker-checker separation

For meaningful outputs:
- one agent can make;
- a different agent or a human checks;
- a human accepts or rejects.

## Agent safety checks

Before activating an agent:
1. Is its purpose specific?
2. Are inputs privacy-safe?
3. Are its tools limited?
4. Does it have a stop condition?
5. Can a human audit its output?
6. Is its authority clearly below the human authority?
7. Can a learner or teacher challenge the result?
