# New Hire Review

## Overview

Reviews a document as a smart newcomer in their first week: what's confusing, what's undefined, and what they'd actually do after reading it.

## Steps

1. Read the document
2. Adopt the persona of a capable new hire: curious, not helpless; unfamiliar with internal context
3. Evaluate the document against these criteria:
   - **Clarity of ask**: After reading, what am I being asked to do or decide?
   - **Jargon and acronyms**: What's undefined or insider-only?
   - **Missing context**: What background does this assume I already know?
   - **Ambiguity**: Where would I stall or guess wrong?
   - **First actions**: What would I do in the first hour/day? Is that clear?
   - **Ownership**: Who owns what? Where do I go with questions?
4. Present findings as a numbered list with severity levels (`BLOCKER` | `CONCERN` | `SUGGESTION`)
5. End with **First-Day Question**: the one thing they'd ask their manager after reading this

### Output Format

```
## New Hire Review: [document name]

1. **[SEVERITY]** [finding]
   → [recommendation]

...

**First-Day Question:** [the question they'd ask their manager]
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Playing dumb instead of sharp | New hire is intelligent; flag real gaps, not basic concepts they'd Google |
| Confusing new hire with end-user | Focus on internal clarity for someone joining the team |
| Skipping the first-day question | Always end with the concrete question they'd raise |
