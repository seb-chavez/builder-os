---
name: using-builder-os
description: Use when starting any session, to know which builder-os skills exist, how a workspace is laid out, and where documents go.
---

# Using builder-os

builder-os is a set of skills for product and consulting work. When a request matches a skill below, use the skill instead of improvising. Red Pen's writing rules are always on.

## Skills

| Skill | Use when |
|-------|----------|
| `red-pen` | A draft is too long, reads like AI wrote it, or is about to be shared |
| `product-brainstorming` | A problem or idea needs exploring before anything is written, solo or as a team workshop |
| `product-researching` | A problem needs investigating before a PRD (manual: `/product-researching`) |
| `product-requirements-drafting` | Writing or updating a PRD or spec |
| `review-panel` | A doc needs one reviewer persona or a panel before it is shared |
| `meeting-prep` | Preparing for a meeting with a person or on a topic |
| `prospecting` | Finding, researching, and ranking prospects, or drafting outreach for the user to send. Reads the workspace's `prospecting/profile.md` |
| `new-workspace` | Starting a new client, employer, or big standalone effort, or a new project inside one |
| `writing-skills` | Creating or editing a builder-os skill |

## Intake before work

Every skill starts by learning what this user needs from this run. A run aimed at the wrong target wastes more than a minute of questions.

- **Ask only what changes the output.** Skip anything the request, the workspace (`AGENTS.md`, `canonical/`, a saved profile), or an earlier answer already says.
- **At most three questions,** in one message as multiple choice when the harness has a question tool; open-ended ones one per message.
- **Nothing missing? Don't ask.** State your assumptions in one line and proceed, so the user can correct them.
- **Save answers that will hold next time** (a profile file, the workspace `AGENTS.md`) so they are not asked again.

## Workspaces

A workspace is one boundary of context: a client, an employer, or a standalone effort. It is its own private repo, with an `AGENTS.md` and a `canonical/` folder:

| Path | Holds |
|------|-------|
| `canonical/accounts/<account>/` | One folder per client or prospect: `account.md`, `people.md`, `projects/<project>/`, `signed/`, and dated account files (`YYYY-MM-DD-outreach.md`) |
| `canonical/accounts/<account>/projects/<project>/` | Project notes (`YYYY-MM-DD-topic.md`), `research/`, `prd.md`, `workshops/` |
| `canonical/partners/<firm>/` | Firms you sell or deliver with: `partner.md`, `people.md`, `signed/` |
| `canonical/vendors/<company>.md` | Companies you or your clients buy from |
| `canonical/contacts.md` | People with no account or partner |
| `canonical/company/` | Your own org. Projects with no account (internal work at an employer) go in `canonical/company/projects/<project>/` |
| `canonical/GOALS.md`, `canonical/PRIORITIES.md` | Current goals and weekly priorities |
| `prospecting/` (repo root) | `profile.md`, `pipeline.md`, `briefs/YYYY-MM-DD-<segment>.md` |

A **project folder** means `canonical/accounts/<account>/projects/<project>/`, or `canonical/company/projects/<project>/` when there is no account. Names are lowercase and hyphenated.

**People** are sections, never one file per person. Each person is a `## Name - role` section in the account's or partner's `people.md`, or in `canonical/contacts.md`. Inside it: `### Recent context`, then `### Meeting notes` with one `#### YYYY-MM-DD - topic` per meeting.

Rules that hold in every workspace:

- **Stay inside the current workspace.** Never read or copy notes from another workspace. Client context must not cross.
- **The workspace `AGENTS.md` wins** on its folder layout, where docs publish, which tools are reachable, and what is confidential. When it maps a path differently from the table above, use its path in every skill and pass it to agents.
- **No `canonical/` here** (for example, someone else's code repo): the workspace skills ask for context instead. Do not create `canonical/` unless the user asks or runs `new-workspace`.
- **Never store raw meeting transcripts.** Synthesize them.
- **Action items live in the issue tracker,** never in people notes, project notes, or meeting notes.

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

Save docs in the workspace in their project folder. Publish only where the workspace `AGENTS.md` says, after a one-line confirmation (title, type, destination). For Notion, follow `rules/doc-formatting.md`.
