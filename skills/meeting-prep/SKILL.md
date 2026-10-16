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
- The meeting is with someone not in `canonical/people/` and you have no project notes mentioning them

## Steps

1. Take the person name or topic from the user's input (e.g., `/meeting-prep jordan` or `/meeting-prep board meeting`)
2. Fuzzy-match the input against filenames in `canonical/people/` and read all matching files
3. Scan recent project notes (`canonical/projects/*/notes/`) for mentions of that person or topic using the Grep tool
4. Read `canonical/GOALS.md` for any relevant items to surface
5. Present a compiled brief with these sections:

### Brief Format

```
## Meeting Prep: [Person/Topic]

### Who They Are
- Role, reports to, communication style, what they care about, pet peeves
(From canonical/people/ file)

### Recent Context
- Last meeting topics and outcomes
- Their current priorities or concerns
(From canonical/people/ meeting notes section)

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
| Reading only the people file and skipping project notes | Always scan `canonical/projects/*/notes/` for mentions too |
| Producing a wall of text | Keep each section to 3-5 bullets max; this is a briefing, not a report |
| Saving the brief to a file | Output to terminal only unless the user explicitly asks to save |
