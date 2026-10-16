---
name: product-requirements-drafting
description: Use when the user wants to write, outline, or update a PRD, product spec, or requirements doc, or to turn a /product-researching bundle (briefing.md, decisions.md) into one. Triggers on "write the PRD", "draft a spec", "update the PRD".
---

# Product Requirements Drafting

Turn a `/product-researching` bundle into a PRD. This skill is the steps only. Every rule about what a good PRD looks like lives in [references/prd-writing.md](references/prd-writing.md) (the rulebook); the structure lives in [templates/prds/prd.md](../../templates/prds/prd.md). Never restate or override those rules here.

## When NOT to use

- No research bundle yet: run `/product-researching` first. Without one, ask the PM whether to research first or draft from what they tell you.
- The PM only wants to understand the problem: read `briefing.md` with them instead.

## Steps

### 1. Find the inputs

**Intake** (see `using-builder-os`; one message, skip what is known): who the main readers are (the engineering team, leadership, a client) and where it will be published. The readers set how much context the Problem section carries; the destination sets the format.

Ask once if not given: the research folder holding `briefing.md` (usually `canonical/projects/<project>/research/`). Its parent is `{project_dir}`.

Pick the deliverable from the request:

- **Outline:** all four Problem subsections, Proposal headings, stub tables.
- **Full PRD:** every section.
- **Update:** an existing `prd*.md` or Notion URL. See step 8.

If `decisions.md` or the PM describes phases (P0 and P1, or several milestones), confirm one PRD per phase before drafting Proposal.

### 2. Read, in this order

1. `briefing.md`, `decisions.md`, `sources.md` in the research folder.
2. [references/research-to-prd.md](references/research-to-prd.md): which research file feeds which section.
3. The rulebook, then the template.
4. [rules/doc-formatting.md](../../rules/doc-formatting.md) if the PRD will be published to Notion.

Read `research-notes/` only for the section you are drafting. Do not re-run research or launch broad discovery; one narrow lookup is fine when a specific fact is missing.

### 3. Gate on open decisions

Read `decisions.md` before writing anything.

- Already answered by the PM in this conversation: record it in the draft.
- Open, but Proposal would have to assume an answer: **stop after Problem.**
- Open and deferrable: put it in Open Questions with an owner. Never assume it silently.

When you stop after Problem, end the deliverable with the open decisions as a **Question | Answer | Blocks** table, using the IDs from `decisions.md`. A Problem section without that table reads as finished and hides that the PM owes a decision.

### 4. Draft Problem and its three subsections

Problem paragraph, then Strategy, Success, and Not trying to solve. Finish all four before Proposal. Run the rulebook's relevance gate and compression pass on the Problem paragraph before moving on.

### 5. Draft Proposal

Approach, how the solution works (with the mock or diagram link if one exists), then requirements as jobs, then dependencies. Translate research and codebase notes into behavior; never paste their vocabulary.

### 6. Draft Plan and References

Timeline, risks, Open Questions last. References from `sources.md`, workspace URLs only. Write the one-line description at the top last.

### 7. Check, then send to a reviewer

1. **Self-check** against the rulebook's **Review checklist** and fix what you find.
2. **Reviewer pass.** If your harness supports sub-agents, start a fresh one. It inherits none of your context, which is the point: the writer is a poor judge of its own draft. Give it this prompt, with the paths filled in:

   > Read-only. Do not edit any files. Read the PRD at `<draft path>` and the rulebook at `<this skill's folder>/references/prd-writing.md`. Check the draft against every item in the rulebook's Review checklist, plus the Length limits table. For the engineer test (items 26 and 27), read each requirement as the engineer who must write the tech spec and list every product question you would need answered before starting. Return only violations, one per line: checklist number, the section, the offending text (quoted, under 15 words), and the fix. If there are none, return "No violations."

   The narrative has a ceiling and the requirements have a floor. Fix length violations by cutting narrative; fix engineer-test violations by adding detail to the acceptance contract, never by cutting.

3. Fix every violation the reviewer returns. If you disagree with one, keep the text and tell the PM why.
4. Repeat the reviewer pass once if the first one returned more than five violations. Stop after two passes.

No sub-agents: do the self-check a second time, reading as the ops reader instead of the author.

For high-stakes docs (client-facing, compliance, money movement), offer `/review-panel` before publishing.

### 8. Update mode

Fetch the existing PRD (for Notion, include discussions and keep open comment threads). Fold new decisions into the jobs already there instead of adding a capability per feature. Then run step 7 on the changed sections.

### 9. Save and publish

Save locally first: `{project_dir}/prd.md`, or `{project_dir}/prd-<slug>.md` for split PRDs. The PM may override the path.

For a full PRD, publish where the workspace `AGENTS.md` says docs go. For Notion: ask where the page should live, show a one-line confirmation (title, Document Type `["PRD"]`, Status `Draft`, destination), wait for a yes unless the PM said "local only," create the page, and return the URL. When updating, prefer `update_content` over `replace_content`.

## Hand back

Tell the PM, in a few lines: what you drafted, where it is saved, what the reviewer flagged and what you changed, and any open decisions as a Question | Answer | Blocks table.

## Examples

```
/product-requirements-drafting canonical/projects/expense-receipts: outline, P0 only
let's write the PRD for the receipt scanning project
update canonical/projects/expense-receipts/prd.md now that we picked option B for D1
```

## Related

| Skill | Relationship |
| ----- | ------------ |
| `/product-researching` | Upstream: produces `briefing.md`, `decisions.md`, `sources.md`, `research-notes/` |
| `/review-panel` | Optional multi-persona review before publishing |
