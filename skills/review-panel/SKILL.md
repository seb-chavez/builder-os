---
name: review-panel
description: Use when a document needs reviewing before it is shared, by a panel of reviewer personas or by one (pessimist, optimist, operator, new hire, budget holder, engineer, executive, champion user). Triggers on "review panel", "panel review", "multiple perspectives", "stress-test a doc", "devil's advocate", "pessimist review", "engineering review of this PRD", "how would an exec read this".
argument-hint: "[path] [persona names, or --budget --engineer --executive --champion-user]"
---

# Review Panel

## Overview

Runs reviewer personas on the same document, then synthesizes consensus, tensions, and prioritized fixes. Each persona lives in [personas/](personas/). With one persona, it is a single review and skips the synthesis.

## Invocation

```
/review-panel [path/to/document]                        # asks which personas
/review-panel [path] --budget --engineer                # default panel plus add-ons
/review-panel [path] pessimist only                     # one persona
```

Natural language works too: "run a review panel on this PRD", "devil's advocate on this proposal", "engineering review of this spec". If no document is given, ask for one. A pasted document counts.

## Workflow

### 1. Ask which personas

| Persona | File | Catches | Default |
|---------|------|---------|---------|
| Pessimist | `personas/pessimist.md` | Unstated assumptions, soft risks, weak evidence | Yes |
| Optimist | `personas/optimist.md` | Upside the doc undersells | Yes |
| Production operator | `personas/operator.md` | What breaks at 2am, who gets paged, rollout gaps | Yes |
| New hire | `personas/new-hire.md` | Jargon and missing context | Yes |
| Budget holder | `personas/budget.md` | Cost, ROI, what it displaces | |
| Engineering lead | `personas/engineer.md` | Feasibility, edge cases, ready to spec? | |
| Executive | `personas/executive.md` | The takeaway, the ask, strategic fit | |
| Champion end-user | `personas/champion-user.md` | Whether real users would adopt it | |

**If the user already named personas or flags** ("pessimist review", "just the engineer", `--budget`), run those and skip the question.

**Otherwise, ask before running anything.** In the same message, also ask (skip what is obvious from the doc or request): who will read it and what decision it supports, and how finished it is (an early draft gets big-picture findings only; a near-final doc gets line-level ones). Pass both answers to every persona. Then: show the table's Persona and Catches columns, recommend the default four plus any add-on the document obviously calls for (a PRD: engineer; a budget ask: budget holder; a doc for leadership: executive), and let the user pick by name, or say "default". Use the harness's multiple-choice question tool if it has one.

### 2. Run them

**One persona:** read its file and follow it in this session. Return its output format and stop. No synthesis.

**Several, with sub-agents:** dispatch one read-only sub-agent per persona in a single parallel batch. Fill in the absolute path of this skill's folder:

```
Read and follow [this skill's folder]/personas/[name].md exactly.

Document: [absolute path, or the pasted text]

Return only that persona's output format. Do not edit files. Do not review from other personas.
```

**Several, no sub-agents:** read each persona file and apply it in turn, keeping outputs under separate headers.

### 3. Synthesize (two or more personas)

Do not paste raw outputs back to back.

```
## Review Panel: [document name]

### Panel
[Who participated]

### Per-persona highlights
#### Pessimist
[Top 2 to 3 findings]

[repeat for each persona]

### Consensus
Findings flagged by 2+ reviewers.

### Tension
Where personas disagree. Name both sides; pick a winner only when one side has a clear factual error.

### Top fixes before sharing
1. [Highest-impact fix]
(3 to 5 items, ordered by impact)
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| One blended review voice | Follow each persona file before synthesizing |
| Synthesizing a single-persona review | One persona returns its own format, nothing more |
| Skipping synthesis on a panel | The user wants consensus, tension, and top fixes |
| Adding personas nobody asked for | Default four, plus add-ons only when flagged |
| Re-reading the doc in the main session after sub-agents | Trust their returns; synthesize from them |
| Inventing persona criteria inline | Always use the persona file |
