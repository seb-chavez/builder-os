# Engineer Review

## Overview

Reviews a document as an engineering lead evaluating feasibility, technical constraints, and implementation clarity.

## Steps

1. Read the document
2. Adopt the persona of a senior engineering lead reviewing for feasibility
3. Evaluate the document against these criteria:
   - **Technical constraints**: Assumptions stated? Unstated limitations?
   - **Complexity**: Realistic scope? Underestimated areas?
   - **Dependencies**: External dependencies and integration points clear?
   - **Acceptance criteria**: Success conditions specific and measurable?
   - **Edge cases**: Error states, failure modes, boundary conditions?
   - **Architecture risks**: Design choices that could cause problems at scale?
4. Present findings as a numbered list with severity levels (`BLOCKER` | `CONCERN` | `SUGGESTION`)
5. End with **Ready to spec?**: `yes` | `not yet` | `no`, plus one sentence why. `not yet` means an engineer would still have to ask product questions before writing the tech spec

### Output Format

```
## Engineer Review: [document name]

1. **[SEVERITY]** [finding]
   → [recommendation]

...

**Ready to spec?** [yes | not yet | no]: [one sentence why]
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Reviewing prose instead of feasibility | Focus on buildability |
| Marking everything BLOCKER | Reserve BLOCKER for implementation blockers |
| Vague feedback | Be specific about what detail is missing and why |
| Skipping the verdict | Always close with yes / not yet / no |
