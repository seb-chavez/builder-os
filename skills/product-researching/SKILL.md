---
name: product-researching
description: Use before drafting a PRD, when a problem needs investigating across chat, the issue tracker, docs, meetings, and the codebase, or when product-requirements-drafting reports that no research bundle exists yet.
disable-model-invocation: true
---

# Product Researching

## Overview

Investigate a problem and leave behind a bundle that `product-requirements-drafting` can turn into a PRD without going back to the sources.

**Core principle: research teaches, it does not decide.** Every scope or architectural fork you find goes into `decisions.md` as an open question with options. The PM resolves them. `product-requirements-drafting` refuses to write Proposal until they are resolved, so a bundle that quietly picked an answer breaks that gate.

## Invocation

`/product-researching <topic or project>`. Manual only, because a full pass makes many Slack, Linear, Notion, and data warehouse calls and writes a folder of files.

## When NOT to use

- The problem is not framed yet. Run `product-brainstorming` first
- You have the bundle and want the document. That is `product-requirements-drafting`
- You need one specific fact. Query it directly rather than running a full pass

## Where the bundle lives

The project folder is `canonical/accounts/<account>/projects/<project>/`, or `canonical/company/projects/<project>/` when there is no account.

```
<project folder>/research/
├── briefing.md
├── decisions.md
├── sources.md
└── research-notes/
    └── <topic>.md
```

`product-requirements-drafting` reads this folder and writes the PRD one level up, at the project root. Other research files may already live here; the four names above are reserved for the bundle. Everything under `canonical/` is gitignored, so the bundle stays local.

## The bundle

`product-requirements-drafting` reads these in order and expects these exact names.

| File | Required | What it holds |
|---|---|---|
| `briefing.md` | Yes | The synthesized answer, in five numbered sections |
| `decisions.md` | Yes | Every open fork, with options and trade-offs. Never resolved here |
| `sources.md` | Yes | Workspace URLs only. Becomes the PRD's References section |
| `research-notes/*.md` | As needed | Raw depth per area. Only create the ones that apply |

## Steps

1. **Confirm scope before investigating. Your first reply is the proposed scope, before reading any file:** the question, which systems you will search, which research notes you expect to produce, and the project folder you will write to. Say which systems you cannot reach. Wait for a yes. A full pass is expensive
2. **Then read local context,** before any outside source: the project folder including any existing `research/`, the account's `account.md` and `people.md`, and `canonical/GOALS.md`. Free, and it shapes better queries
3. **Gather.** Work source by source (below), capturing URLs as you go rather than reconstructing them later
4. **Write `research-notes/` as you gather**, one file per area. Raw and specific. This is the layer allowed to be technical
5. **Write `briefing.md` last.** It synthesizes the notes; it does not accumulate during gathering
6. **Write `decisions.md`.** Every fork you hit, still open
7. **Write `sources.md`.** Workspace URLs only
8. **Report what you found and what is thin**, then hand off to `product-requirements-drafting`

## Where to look

| Source | Good for |
|---|---|
| Team chat | Why a decision was made, who objected, what broke |
| Issue tracker | Tickets, milestone dates, bug patterns, current state |
| Data warehouse | Volume, dollars, frequency. The numbers that size the problem |
| Docs (Notion MCP) | Existing PRDs, specs, and strategy docs |
| Meetings (notes in `canonical/`, or a note-taker MCP if one is connected) | What stakeholders actually said, and their positions |
| Codebase | How it works today, what the constraints are |

Access to the first three depends on the company. Check the workspace `AGENTS.md` for what is set up, and ask rather than assuming a system is reachable.

## briefing.md

Five numbered sections, plus a summary at the top. `product-requirements-drafting` maps them onto PRD sections by number, so keep the numbering.

| Section | Contents |
|---|---|
| Executive Summary | Three to five sentences. The problem, the stakes, the shape of the answer |
| §1 World Today | How the workflow runs now, end to end. Where it breaks |
| §2 Who Is Affected | Operators, customers, internal teams. What each one experiences |
| §3 Evidence | Volume, dollars, frequency, dates. Every number with its source |
| §4 Gaps and Risks | What is missing, what breaks if nothing ships, what could go wrong if something does |
| §5 Approach Options | Pointers only. Directions worth considering, never a chosen one |

Write it so a PM who was not in any of the meetings can brief someone else from it.

## decisions.md

One entry per fork. The shape matters more than the prose:

```markdown
## D1: <the question, phrased as a question>

**Options**
- A: <option>. <trade-off>
- B: <option>. <trade-off>

**Leaning:** <which and why, one sentence. A leaning is not a decision>
**Blocks:** <which PRD section cannot be written until this is resolved>
**Status:** OPEN
```

Keep `Status: OPEN` until the PM says otherwise. `product-requirements-drafting` may draft the Problem section while decisions are open, but stops before Proposal until the ones Proposal depends on are resolved.

## sources.md

Workspace URLs a teammate can open: Notion, Linear, Gong, Incident.io, Confluence, Figma. Group by area, one line each, with enough label to know why it mattered.

Never list local files or repo paths. This file becomes the PRD's References section, and the published doc has to stand alone.

## research-notes/

Create only what applies. `product-requirements-drafting` reads these on demand for specific PRD sections.

| File | Feeds |
|---|---|
| `codebase.md` | How it works today, technical constraints, requirements |
| `ops-current-state.md` | The manual workflow being replaced |
| `existing-tools.md` | What is already built, internal or vendor |
| `stakeholder-context.md` | Teams, vendors, timelines, dependencies |
| `regulatory.md` | Compliance requirements, with primary sources cited |
| `bug-catalog.md` | Known failure patterns, which become PRD risks |

These may be as technical as the source material. `product-requirements-drafting` translates them into product language, so do not pre-flatten them here.

## Confidence labels

Mark any high-stakes claim (compliance, dollars, volume) so drafting knows what it can assert:

- `[DATA VERIFIED]` you saw the number in the system named
- `[INTERPRETATION VERIFIED]` a human confirmed your reading of it

Unlabeled means unverified. Never label something you inferred.

## Common mistakes

| Mistake | Fix |
|---|---|
| Resolving a decision instead of posing it | `decisions.md` entries stay OPEN. The PM picks, and drafting's Proposal waits on it |
| Writing `briefing.md` while gathering | Write it last. Notes accumulate, syntheses do not |
| Reconstructing URLs afterward | Capture into `sources.md` as you go, or you will not find them again |
| Naming a file something other than the contract | `product-requirements-drafting` looks for exact names and stops when they are missing |
| Flattening technical detail into notes | Notes stay raw. Drafting does the translation, and it needs the specifics |
| A number without a source | Every figure in §3 names where it came from, or it cannot be used |
| Running a full pass for one fact | Query it directly. This skill is for a whole problem |

## Handoff

Report which sections are thin and which decisions are open, then stop. `product-requirements-drafting` is the next step. It can draft the Problem section right away; Proposal waits until the PM resolves the `decisions.md` entries it depends on.
