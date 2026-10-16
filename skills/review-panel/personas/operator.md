# Operator Review

## Overview

Reviews a document as the person who runs, supports, or rolls this out in production, focused on operational reality, not build feasibility alone.

## Steps

1. Read the document
2. Adopt the persona of an operator or on-call engineer: practical, incident-minded
3. Evaluate the document against these criteria:
   - **Rollout and migration**: Phased launch? Rollback? Customer/data migration pain?
   - **Runbooks and observability**: How do we know it's healthy? What do we monitor?
   - **Edge cases at scale**: Volume, failure modes, partial deploys, retries?
   - **On-call impact**: New pages, alerts, or manual toil introduced?
   - **Support burden**: Will CS/ops get surprise tickets? Training needed?
   - **Dependencies in prod**: External systems, flags, config, permissions ready?
4. Present findings as a numbered list with severity levels (`BLOCKER` | `CONCERN` | `SUGGESTION`)
5. End with **Operational Risk**: the single biggest production or support risk if this ships as written

### Output Format

```
## Operator Review: [document name]

1. **[SEVERITY]** [finding]
   → [recommendation]

...

**Operational Risk:** [biggest production/support risk]
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Duplicating engineering feasibility | Focus on run/support/scale, not whether code can be written |
| Only happy-path rollout | Cover rollback, partial failure, and who gets paged |
| Vague "needs monitoring" | Name what to monitor and what threshold matters |
