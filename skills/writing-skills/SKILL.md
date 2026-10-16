---
name: writing-skills
description: Use when creating a new skill for builder-os, editing an existing SKILL.md, deciding whether a recurring workflow is worth turning into a skill, or working out why a skill never fires when expected.
---

# Writing Skills

## Overview

A skill is a reusable reference for a technique. It is not a record of how you solved something once.

**Core principle: write the skill against a failure you actually watched.** If you have not seen the current behavior fall short, you are guessing at what to teach, and the skill will document your intentions instead of fixing anything.

## Invocation

`/writing-skills` (or automatically, when you start creating or editing a `SKILL.md`).

## When to write one

Write a skill when:

- You have run the same workflow several times and corrected it the same way each time
- The technique was not obvious to you the first time through
- The correction is a judgment call, not something a script could enforce

Do not write a skill for:

- A one-off task
- A rule that is always true (that belongs in `using-builder-os`, or a workspace's `AGENTS.md` if it is about one client)
- Formatting or prose conventions (those belong in `rules/`)
- Anything CI or a script in `scripts/` could check mechanically

Rule of thumb: `using-builder-os` is what is always true. `rules/` is how output should look. A skill is what to do when a specific job comes up.

## When NOT to use

- Editing `README.md`, `rules/`, or a workspace's `AGENTS.md`. Those are not skills
- Adding a template to `templates/`. A template is a blueprint, not a playbook
- Quick fixes to an existing skill's typos or links

## Before you write: find the failure

**Your first reply asks for the failure.** Before exploring files or drafting anything, ask: what went wrong the last time this task was done without a skill? A past output that needed fixing, or a cold run you can do now, is what the skill gets written against.

**Outside the builder-os repo**, do not stop to look for it. Still lead with the failure question, write the skill where the user wants it, and name the repo checklist below as the step to do once it moves into builder-os.

Run the task without the skill and write down what actually happened, verbatim.

The cheap version for PM work: take a real artifact you already know the right answer for (a PRD you have already revised, a meeting you have already summarized, a doc you already sent back for changes), ask for the output cold, and note every place it went wrong. Those specific gaps become the skill's content.

Skip this step and you get a skill full of advice nobody needed.

**If the cold run is already correct, stop. There is no skill to write.**

For skills that enforce a discipline someone will be tempted to skip, the baseline needs pressure applied. See `references/testing-skills.md`.

## Skill types in builder-os

| Type | Examples | What it needs |
|---|---|---|
| Workflow | `meeting-prep`, `new-workspace` | Numbered steps and a confirmation gate before any write |
| Document | `product-requirements-drafting` | The template it fills, the rules it obeys, its upstream input |
| Review persona | a file in `review-panel/personas/`, not a skill | Whose voice, what they optimize for, the output shape |
| Reference | Domain notes | Retrieval structure. Tables beat prose |

## Structure

```markdown
---
name: skill-name
description: Use when [triggering conditions]
---

# Skill Name

## Overview
What it is, and the core principle. Two sentences.

## Invocation
`/skill-name`, or the natural language that should trigger it.

## When NOT to use
The neighboring skills this gets confused with.

## Steps
Numbered, with a confirmation gate before anything is written (or, for an unattended skill, a write log and a review file instead).

## Quick reference
A table for scanning.

## Common mistakes
| Mistake | Fix |
```

Keep everything inline. Split into `references/` only for heavy reference material (100+ lines) or a reusable script.

## Writing the description

The highest-leverage field in the file. It decides whether the skill is ever found.

**The description says when to use the skill. Never what it does.**

If it summarizes the workflow, that summary becomes a shortcut: it gets followed instead of the skill body, and the actual steps get skipped.

```yaml
# Bad. Summarizes the workflow, so the body gets skipped
description: Drafts a PRD by pulling research, filling the template, then pushing to Notion

# Bad. First person
description: I can help you write PRDs

# Good. Triggering conditions only
description: Use when turning research output into a PRD, or when the user asks for a PRD, product spec, or requirements doc
```

Rules:

- Third person
- Concrete triggers, including phrases you would actually type
- Under 500 characters
- No workflow summary

## Decide model invocation deliberately

**REQUIRED.** Pick one and know why.

| Setting | Effect | Use for |
|---|---|---|
| (omit the field) | Fires on its own when the description matches, and you can still type `/name` | Skills whose value is catching something you did not think to ask for |
| `disable-model-invocation: true` | Only fires when you type `/name` | Expensive, destructive, or externally visible skills |

Some builder-os skills are manual-only. That is defensible for skills that write files or post to Slack. It is the wrong default for a skill meant to catch you before you start down the wrong path. A manual-only skill's trigger phrases do nothing, so do not spend effort writing them.

## Match the form to the failure

Classify the failure before writing the guidance. The form that fixes one kind measurably worsens another.

| Failure | Right form | Wrong form |
|---|---|---|
| Knows the rule, skips it under pressure | Prohibition plus a rationalization table | Soft guidance ("prefer", "consider") |
| Complies, but the output is the wrong shape | A recipe: state what the output is, in order | A list of prohibitions |
| Leaves out a required element | A REQUIRED slot in the template itself | Prose reminders near the template |
| Behavior should depend on a condition | A conditional keyed to something observable | An unconditional rule plus exceptions |

Prohibitions backfire on shaping problems. Given a competing incentive, "do not do X" gets negotiated. A recipe leaves nothing to negotiate: the output either matches the stated shape or it does not.

Two rules whichever form you pick:

- **No nuance clauses.** "Do not X unless it matters" reopens the argument. Write a real exception as its own conditional.
- **Exemption clauses do not scope.** "This limit does not apply to tables" still suppresses tables. Restructure so the rule cannot reach the exempt part.

## Bulletproofing

Only for skills enforcing a discipline someone will be tempted to skip. Skip this section for reference and workflow skills.

- Forbid the specific workarounds, not just the behavior
- State early that violating the letter is violating the spirit. That closes a whole class of argument
- Build a rationalization table from what you actually saw in the cold run, quoted
- Add a red flags list so the reader can catch themselves mid-rationalization

## Repo checklist

**REQUIRED for every new skill.** The first three are the ones that get forgotten.

- [ ] Add a row to the skills table in **both** `skills/using-builder-os/SKILL.md` and `README.md`. CI fails if they disagree
- [ ] Restart the session after `/plugin update`. Skills do not hot-reload
- [ ] Add test cases in `skills/<name>/evals/`: one that should start the skill, one that should not (or, for a slash-only skill, one that runs the command), and one for its most important rule. Copy an existing skill's cases for the format, then run `./scripts/test-skills.sh <name>`
- [ ] Starts with an intake: the few questions that change the output, skipped when the request already answers them (rule in `using-builder-os`)
- [ ] Frontmatter has `name` and `description`, under 1024 characters total
- [ ] Model invocation decided deliberately, not by accident
- [ ] Prose follows `rules/red-pen.md`. No em dashes; CI checks
- [ ] Run the skill on the real artifact from your cold run, and compare
- [ ] Feature branch and PR. Never commit a skill straight to `main`

## Common mistakes

| Mistake | Fix |
|---|---|
| Writing the skill before watching anything fail | Run the cold pass first. Otherwise you are documenting intentions |
| Description summarizes the workflow | Triggering conditions only. The summary becomes a shortcut past the body |
| Skill duplicates `using-builder-os` | If it is always true, it belongs there |
| Forgetting the skills table | `using-builder-os` never tells the agent the skill exists |
| Narrative writing ("last quarter we found...") | Skills are reference, not story. Cut to the technique |
| Adding a skill because the topic feels important | Importance is not reuse. Three real uses, or skip it |

## Reference

- `references/testing-skills.md` for pressure-testing discipline skills
- [Anthropic's skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) for the official guidance

## Attribution

Adapted from `superpowers:writing-skills` by Jesse Vincent, MIT licensed.

Changes for builder-os: removed the hard dependency on `superpowers:test-driven-development` (the testing method is now self-contained in `references/testing-skills.md`), dropped the graphviz flowchart tooling, reframed examples from engineering to PM work, and added the repo checklist and the model-invocation decision.
