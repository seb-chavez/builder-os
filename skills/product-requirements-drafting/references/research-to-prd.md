# Research bundle to PRD sections

Which research file feeds which PRD section. The research bundle is the only primary source for facts; the PRD compresses it and commits scope. Writing rules live in `prd-writing.md` next to this file.

## Inputs (`{research_dir}/`)

| File | Use |
| ---- | --- |
| `briefing.md` | Facts for Problem and Success. Required: if it is missing, stop and run `/product-researching`. |
| `decisions.md` | Open forks. Resolve or park in Open Questions before Proposal. |
| `sources.md` | Workspace URLs for References. Never link this file itself. |
| `research-notes/*.md` | Optional detail on demand. Translate before writing, especially `codebase.md`. |

## Section mapping

| PRD section | Research sources | Note |
| ----------- | ---------------- | ---- |
| Reviewers | None | Ask the PM. Never invent names. |
| One-line description | `briefing.md` Executive Summary | Write last |
| Problem | `briefing.md` World Today, Who Is Affected, Gaps | Only the gap and its direct consequence |
| Strategy | `briefing.md` cost of waiting; `stakeholder-context.md`; goals if the PM points to them | Business consequence, not a milestone list |
| Success | `briefing.md` Evidence (baselines), Gaps and risks | Baselines from our own records |
| Not trying to solve | `decisions.md` scope forks; `briefing.md` Gaps | Product terms |
| How we intend to solve it | `decisions.md` after the PM chooses | Why this beats the alternative |
| How the solution works | `codebase.md`, `existing-tools.md`; mocks named in `stakeholder-context.md` | Operator flow first |
| Requirements | `codebase.md` (what exists), `regulatory.md` (must-haves), `decisions.md` | Behavior, not implementation |
| Dependencies | `stakeholder-context.md` | Team and vendor names are fine |
| Timeline | `stakeholder-context.md`, tracker dates | Home for milestone dates |
| Risks | `bug-catalog.md`, `briefing.md` Gaps | Plain language |
| Open Questions | Leftovers from `decisions.md`, gaps found while drafting | |
| References | `sources.md` | Workspace URLs only |

## Multiple PRDs

When the PM splits delivery into phases: one file per phase (`prd-p0.md`, `prd-p1.md`). Shared Problem facts get one sentence and a link to the sibling. Each phase's Not trying to solve names the other.

## Confidence labels

Keep research's `[DATA VERIFIED]` and `[INTERPRETATION VERIFIED]` judgments in mind for high-stakes claims (compliance, money, volume). In the PRD, prefer a sourced sentence with a link over inline tags unless the PM wants the tags.

If the research looks wrong, fix the research files or add an Open Question. Do not re-litigate research inside Proposal.
