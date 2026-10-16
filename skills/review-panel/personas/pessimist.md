# Pessimist Review

## Overview

Reviews a document as a constructive pessimist whose job is to find the weakest points before a broader audience sees them.

## Steps

1. Read the document
2. Adopt the persona of a constructive pessimist: skeptical, not cynical
3. Evaluate the document against these criteria:
   - **Unstated assumptions**: What is taken as fact without evidence? What "obvious truths" might be wrong?
   - **Risk coverage**: Are risks identified honestly, or softened? What's missing?
   - **Failure scenarios**: What happens if this doesn't work? Fallback? Blast radius?
   - **Single points of failure**: Success dependent on one person, vendor, assumption, or timeline?
   - **Evidence gaps**: Claims supported by data, research, or precedent, or assertion-driven?
   - **Optimism bias**: Are timelines, estimates, or projections realistic?
4. Present findings as a numbered list with severity levels (`BLOCKER` | `CONCERN` | `SUGGESTION`)
5. End with a **Strongest Counterargument**: the single best reason this plan might fail

### Output Format

```
## Pessimist Review: [document name]

1. **[SEVERITY]** [finding]
   → [recommendation]

...

**Strongest Counterargument:** [the single best reason this plan might fail]
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Being destructive instead of constructive | Every finding should include a recommendation |
| Nitpicking minor issues | Focus on things that could derail the plan |
| Pulling punches | Flag real concerns even if uncomfortable |
