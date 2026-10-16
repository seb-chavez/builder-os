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

Use the paths in the workspace `AGENTS.md` when it gives them. Otherwise people notes are one file each in `canonical/people/`, or `## Name - role` sections in shared files (an account's `people.md`, a `contacts.md`).

## Steps

1. Take the person name or topic from the user's input (e.g., `/meeting-prep jordan` or `/meeting-prep board meeting`)
   **Intake** (see `using-builder-os`; skip what the request says): what the meeting is for (a decision, an update, a relationship, a sale, an interview), and what the user wants to walk out with. Shape the brief around the answer: lead with what supports their ask, and add a "Your ask" line at the top.
2. Find the person two ways and read every match: fuzzy-match the input against filenames in `canonical/people/`, and Grep `^## .*<name>` across `canonical/` for sections in shared files. For a section, read only that section (down to the next `## ` heading)
3. Scan recent project notes (`canonical/projects/*/notes/`) for mentions of that person or topic using the Grep tool
4. Read `canonical/GOALS.md` for any relevant items to surface
5. Present a compiled brief with these sections:

### Brief Format

```
## Meeting Prep: [Person/Topic]

### Who They Are
- Role, reports to, communication style, what they care about, pet peeves
(From the person's file or section)

### Recent Context
- Last meeting topics and outcomes
- Their current priorities or concerns
(From the person's meeting notes)

### Relevant Project Activity
- Recent decisions or progress related to this person/topic
(From canonical/projects/*/notes/)

### Goals to Surface
- Any active goals relevant to the meeting
(From canonical/GOALS.md)
```

6. Output the brief in the terminal only; this is ephemeral prep, not a saved document

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Matching only filenames and missing a person kept as a section in `people.md` or `contacts.md` | Always Grep `^## ` headings too |
| Reading only the people file and skipping project notes | Always scan `canonical/projects/*/notes/` for mentions too |
| Producing a wall of text | Keep each section to 3-5 bullets max; this is a briefing, not a report |
| Saving the brief to a file | Output to terminal only unless the user explicitly asks to save |
