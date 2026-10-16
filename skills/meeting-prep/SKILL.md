---
name: meeting-prep
description: Use when preparing for a meeting and need context on a person, team, or topic. Triggers on "prep for my meeting", "meeting with [name]", "prep me for", "what do I need to know about [person]".
---

# Meeting Prep

## Overview

Compiles a briefing from the workspace's `canonical/` folder before a meeting. Pulls person context, recent project activity, and relevant goals into a single brief. Action items live in your issue tracker, not here.

Only read the current workspace. Never pull notes from another client's workspace into this brief.

## When NOT to use

- You already have the context you need
- No `canonical/` folder here: say so, ask the user for what they know about the person or topic, and offer `new-workspace` if this should become a workspace
- The meeting is with someone who has no people notes and no project notes mentioning them

## Where people live

Each person is a `## Name - role` section in an account's or partner's `people.md` (`canonical/accounts/*/people.md`, `canonical/partners/*/people.md`) or in `canonical/contacts.md`. Older workspaces may still keep one file per person in `canonical/people/`; check there too.

## Steps

1. Take the person name or topic from the user's input (e.g., `/meeting-prep jordan` or `/meeting-prep board meeting`)
   **Intake** (see `using-builder-os`; skip what the request says): what the meeting is for (a decision, an update, a relationship, a sale, an interview), and what the user wants to walk out with. Shape the brief around the answer: lead with what supports their ask, and add a "Your ask" line at the top.
2. Grep `^## .*<name>` (case-insensitive, fuzzy on the name) across `people.md` and `contacts.md` under `canonical/`, and read only each matching section, down to the next `## ` heading. When the person sits in an account's or partner's `people.md`, also skim that folder's `account.md` or `partner.md`. Fallback for older workspaces: fuzzy-match filenames in `canonical/people/`
3. Grep recent project notes (`canonical/accounts/*/projects/` and `canonical/company/projects/`) for mentions of that person or topic
4. Read `canonical/GOALS.md` for any relevant items to surface
5. Present a compiled brief with these sections:

### Brief Format

```
## Meeting Prep: [Person/Topic]

### Who They Are
- Role, reports to, communication style, what they care about, pet peeves
(From the person's section)

### Recent Context
- Last meeting topics and outcomes
- Their current priorities or concerns
(From the person's meeting notes)

### Relevant Project Activity
- Recent decisions or progress related to this person/topic
(From project notes under accounts/*/projects/ and company/projects/)

### Goals to Surface
- Any active goals relevant to the meeting
(From canonical/GOALS.md)
```

6. Output the brief in the terminal only; this is ephemeral prep, not a saved document

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Looking for a file per person and missing their section | Grep `^## ` headings in `people.md` and `contacts.md` first |
| Reading the whole `people.md` or `contacts.md` | Read only the matching section |
| Reading only the person's notes and skipping project notes | Always grep project folders for mentions too |
| Producing a wall of text | Keep each section to 3-5 bullets max; this is a briefing, not a report |
| Saving the brief to a file | Output to terminal only unless the user explicitly asks to save |
