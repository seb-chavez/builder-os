---
name: using-product-os
description: Use when starting any session, to know which product-os skills exist, how a workspace is laid out, and where documents go.
---

# Using product-os

product-os is a set of skills for product and consulting work. When a request matches a skill below, use the skill instead of improvising. Red Pen's writing rules are always on.

## Skills

| Skill | Use when |
|-------|----------|
| `red-pen` | A draft is too long, reads like AI wrote it, or is about to be shared |
| `product-brainstorming` | A problem or idea needs exploring before anything is written, solo or as a team workshop |
| `product-researching` | A problem needs investigating before a PRD (manual: `/product-researching`) |
| `product-requirements-drafting` | Writing or updating a PRD or spec |
| `review-panel` | A doc needs one reviewer persona or a panel before it is shared |
| `meeting-prep` | Preparing for a meeting with a person or on a topic |
| `new-workspace` | Starting a new client, employer, or big standalone effort, or a new project inside one |
| `writing-skills` | Creating or editing a product-os skill |

## Workspaces

A workspace is one boundary of context: a client, an employer, or a standalone effort. It is its own private repo, with an `AGENTS.md` and a `canonical/` folder:

| Path | Holds |
|------|-------|
| `canonical/people/firstname-lastname.md` | Stakeholder notes |
| `canonical/projects/<project>/` | Project notes (`YYYY-MM-DD-topic.md`), research, PRDs |
| `canonical/company/`, `canonical/teams/` | Org context |
| `canonical/GOALS.md`, `canonical/PRIORITIES.md` | Current goals and weekly priorities |

Rules that hold in every workspace:

- **Stay inside the current workspace.** Never read or copy notes from another workspace. Client context must not cross.
- **The workspace `AGENTS.md` wins** on where docs publish, which tools are reachable, and what is confidential.
- **No `canonical/` here** (for example, someone else's code repo): the workspace skills ask for context instead. Do not create `canonical/` unless the user asks or runs `new-workspace`.
- **Never store raw meeting transcripts.** Synthesize them.
- **Action items live in the issue tracker,** never in people files, project notes, or meeting notes.

## Documents

When asked for a document, fill the matching template from this plugin's `templates/` folder (two levels up from this file). If the type is unclear, ask which one.

| Request | Template |
|---------|----------|
| PRD, spec | `product-requirements-drafting` skill |
| Discovery questions, customer interview | `templates/discovery/discovery-questions.md` (rules in `timeboxing.md` beside it) |
| Agenda | `templates/meetings/agenda.md` |
| Meeting notes | `templates/meetings/meeting-notes.md` |
| Decision log | `templates/meetings/decision-log.md` |
| Project brief | `templates/strategy/project-brief.md` |
| Status update | `templates/strategy/status-update.md` |
| Roadmap | `templates/strategy/roadmap.md` |

Save docs in the workspace under `canonical/projects/<project>/`. Publish only where the workspace `AGENTS.md` says, after a one-line confirmation (title, type, destination). For Notion, follow `rules/doc-formatting.md`.
