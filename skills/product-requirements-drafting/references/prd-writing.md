# PRD Rules

The only place PRD rules live. `templates/prds/prd.md` holds the structure; the `product-requirements-drafting` skill holds the steps. If either disagrees with this file, this file wins. Red Pen's rules apply on top, plus `rules/doc-formatting.md` when publishing to Notion.

Examples below use one running case: employees whose expense claims are rejected as "missing receipt" when the receipt is attached but unreadable.

## Voice and audience

Write like a senior PM explaining a messy domain to a smart non-engineer. Plain sentences, concrete examples. Distill complexity; do not reproduce it.

The PRD is a product document for mixed readers: PM, ops, eng leads, client stakeholders. It is not a technical design doc, an architecture note, or a tracker export. Engineering writes the TDD with implementation vocabulary; the PRD gives constraints and acceptance outcomes.

| Section | Language |
| ------- | -------- |
| Problem, Strategy, Success, Not solving | Business and operator terms only |
| Proposal narrative | Technical context only where scope needs it |
| Requirements | Testable outcomes for people and the business |
| Plan, Dependencies | Team, vendor, and system names are fine |

**Ops reader test:** could the ops team read a line and know what breaks, or what "done" looks like, without knowing our codebase? If not, simplify.

**Translation rule:** when research names a contract, adapter, cron, or ticket, ask *what breaks for a person if we do not ship this?* Write that answer. Link the source in References.

## Section order

1. **Problem**, with its Strategy, Success, and Not solving subsections. Finish all four before Proposal.
2. **Proposal**: approach, how it works, requirements, dependencies.
3. **Plan**: timeline, risks, Open Questions last.
4. **References**: one list at the very bottom.

## Length limits

These are hard caps. Detail that does not fit belongs in a job story.

| Section | Limit |
| ------- | ----- |
| One-line description | One sentence on the outcome, written last |
| Problem | One paragraph, 2 to 4 sentences |
| Strategy | One short paragraph; at most one small table |
| Success | One sentence, then one metrics table |
| Not trying to solve | One opening sentence, then 5 to 10 bullets |
| How we intend to solve it | Three sentences |
| How the solution works | Eight one-line bullets at most, plus a mock or diagram link |
| Requirements | 3 to 8 jobs; each acceptance paragraph three sentences at most |

## Problem

**Goal:** a reader who never opens the tracker can repeat the problem and its stakes from this section alone.

Weave what is broken, who bears the cost, and why it matters into normal prose, the way you would say it in Slack to a cross-functional lead. Stop once the core gap and its direct consequence are clear. No subheaders, bullets, bold audience labels, or solutions.

| Wrong | Right |
| ----- | ----- |
| "Spec ready 2026-09-25, scoping 2026-10-30, launch 2027-04-01. Audit in Q1." | "Expense claims whose receipt the scanner cannot read are rejected as 'missing receipt' even though one is attached, so employees wait weeks to be repaid money they already spent." |
| "**Employees:** delayed repayment. **Reviewers:** backlog. **Finance:** audit exposure." | "Reviewers work a permanent backlog, employees wait weeks to be repaid, and every wrong rejection is a claim finance cannot explain to the auditor." |
| "Employees upload a photo. The scanner reads it. The scan fails. Review sees the same scan. The claim is rejected." | "Claims fail the receipt check when the scanner cannot read the photo, and manual review is blind to the same photo." |

**Relevance gate.** A fact goes in Problem only if all three hold: it describes the current gap or its direct consequence; it concerns this exact workflow; and the reader would misunderstand why the work matters without it. Route everything else:

| Fact | Goes to |
| ---- | ------- |
| File formats, ownership, funding model, mapping drafts | Proposal or Open Questions |
| Vendor status, readiness work | Plan or Dependencies |
| Pilot dates, launch windows | Strategy or Plan |
| Rates from another product or integration | Omit, unless the same cause is proven and the number changes a requirement or target |

**Compression pass.** For each sentence, name its new fact. Delete or merge any sentence that repeats a neighbor. Drop background that does not change the problem, stakes, or scope. If the paragraph builds toward its point, move the point to the front.

## Strategy: how does this connect to our priorities?

Say which company or client priority this serves and why now, in business terms: client onboarding, an incident, a regulatory finding, ops load at scale. A date or milestone appears only when tied to the consequence of hitting or missing it. Schedules are never the "why."

Do not repeat the Problem, describe the build, list tracker milestone names, or name individuals.

## Success: what does success look like?

One sentence on when success is achieved and the bar in outcome terms. Then one table, small enough that every row proves this build worked.

**Columns:** Type | Metric | Description. Description opens with one plain sentence, then `<br>`-separated lines for **Baseline**, **Target**, and **How we measure**.

| Type | Role |
| ---- | ---- |
| Primary | Did we solve the problem? Usually one row. |
| Secondary | Validates a key bet. Zero to two rows. |
| Guardrail | Downside we will not accept. Ship is blocked if breached. |

**Every metric is measurable from our own systems:** product timestamps, logs, stored records. Never ask a customer, bank, or auditor to track new data for us. Records they already keep and would hand over anyway are fine as a baseline.

**Every target carries a reason.** Source the baseline (report, ticket, dashboard, incident). With no baseline, as in 0-to-1 work, state the hypothesis behind the target. With a single customer, frame the metric as pass or fail.

Prefer absolute limits over percentages when volume grows: "under 50 manual reviews per week," not "under 10% of claims" when 10% of a growing book swamps the team. Binary outcomes are fine ("zero duplicate repayments").

**5am test:** a tired reader understands every row alone. Short plain Metric name; Description spells out any difference between related rows.

**Metrics are not requirements.** Messaging copy, observability, internal SLAs, and eng ticket volume are requirements. No function names, states, log fields, or named dashboards; engineering picks instrumentation.

## Not trying to solve

Open with what this delivery covers and by when, in product terms. Then 5 to 10 bullets, each **Topic:** what is excluded and why (timeline, another team owns it, unverified, follow-on). A dependency on another team means we need their answer but do not build their side. If unsure whether something is true, it is an Open Question, not an exclusion.

## Proposal

**How we intend to solve it:** three sentences. The approach, and why it beats the alternative we considered.

**How the solution works:** link the mock or diagram, then at most eight one-line bullets. If a bullet needs explaining, it is a requirement.

A sentence that names a screen, API, file format, or workflow step the team will build belongs in Proposal, never in Problem or Success.

## Requirements

Every requirement is a job. Open each capability with a job story, then give the acceptance contract beneath it. This section carries the detail, so it is allowed to be long.

```
### (P0) <capability name>

**When** <situation>, **<job-doer>** **wants to** <motivation>, **so they can** <outcome>.
```

**Job story rules:**

- **One job per capability.** If the story needs "and" to hold together, it is two jobs.
- **The situation is a moment in the job-doer's day**, never the moment they open the product.
- **The outcome is something a person wants**, not something the system does.
- **Name the job-doer by role**: the reviewer, the approver, the auditor. Never an individual.
- **A job nobody does is not a requirement.** If the only doer is the system, it is plumbing inside another job's acceptance.
- **If you cannot write the story, you do not understand the requirement yet.** Never bolt one on to satisfy the format.

| Wrong | Right |
| ----- | ----- |
| "When a user wants to upload receipts, they want to upload receipts, so they can have receipts uploaded." | "When a receipt is crumpled or faded, the employee wants to know before submitting that it will not scan, so they can retake the photo instead of waiting two weeks for a rejection." |
| "So the scan results are stored correctly." | "So they can give the auditor a number that comes out the same in March as it did in December." |
| "When using the receipt review feature..." | "When the auditor asks why a claim was paid, six months after it was approved..." |

**Acceptance contract.** After the story, one paragraph of three sentences at most: where the job starts, where it ends, and what proves it is done. Then only the structure the job needs:

- A table for required business fields, records, or entities.
- Bullets for actions a person takes or information they see.
- A numbered list for ordered statuses or stages.
- A closing paragraph for validation, exceptions, duplicate prevention, or audit history.

Make product decisions explicit where research supports them: system of record, persistent versus per-transaction data, user-visible statuses, imposed formats or controls, and failure behavior. Name capabilities after the behavior, not an adapter, class, or ticket. Keep one workflow in one capability rather than twenty fragments. Never specify classes, tables, jobs, or APIs.

**Folding in new input.** When new decisions or design notes land in an existing PRD, fold them into the jobs already there. Do not add a capability per feature. Re-check the limits above before showing the result.

## Plan

**Timeline** is where milestone dates live. Add the business consequence when it helps ("if this slips past March, we carry another quarter of wrongly rejected claims").

**Risks** stay in plain language; technical mitigations belong in Proposal or the TDD.

**Open Questions** come last. Each has an owner who can answer it. When answered, move the fact into Problem or Proposal and record the resolution.

**Decisions.** Whenever open decisions are presented, in a PRD or a drafting handoff, use a table: **Question | Answer | Blocks**. Questions in plain words with a concrete scenario, never jargon shorthand. Leave Blocks empty once a decision is answered, so open ones stand out.

## People and names

The PRD is about problems, constraints, and outcomes, not who said what. No individual names in Problem, Strategy, Success, Proposal narrative, or Risks. Names are fine only in the Reviewers table and in Owner or POC columns, and a role is better there too.

Wrong: "INC-123 made refund safety non-negotiable for Dana Kim." Right: "A recent incident made refund safety a hard constraint," with the incident linked in References.

Use team names only when the dependency is the point. Never turn stakeholder quotes or internal debates into narrative; state the constraint as a fact.

## References

One section at the very bottom, after Open Questions. Workspace URLs any teammate can open: Notion, the tracker, call recordings, incident tools, Confluence, Figma. Ticket IDs appear here as links, never as raw IDs in body prose.

Never link local files (`briefing.md`, `decisions.md`, `sources.md`), repo paths (`canonical/`), or instruction files. Never add a formatting or repo footer.

## Formatting

- No em dashes anywhere.
- `approx.`, not `~`, in Notion-bound docs (tildes render as strikethrough).
- Delete all italic template instructions before sharing.
- Importance sentences, AI vocabulary, and summary endings are out (Red Pen's cut-on-sight list).

## Review checklist

The drafter self-checks against this list, and the `product-requirements-drafting` reviewer pass checks against it. Every item is a violation to fix.

**Length and structure**
1. A section exceeds its limit in **Length limits**.
2. Proposal was drafted before all four Problem subsections were done.
3. Open Questions are not last in Plan, or References are not at the very bottom.

**Problem and Strategy**
4. Problem has subheaders, bullets, bold audience labels, or a second paragraph.
5. Problem or Success contains solution language.
6. A Problem fact fails the relevance gate, or two adjacent sentences carry the same fact.
7. The "why" is a schedule: milestones, dates, or roadmap labels.
8. A fact comes from another product or integration without a proven shared cause.

**Success**
9. A metric needs data the customer, bank, or auditor would have to track for us.
10. A target has no sourced baseline and no stated hypothesis.
11. A percentage target ignores growing volume.
12. A row is really a requirement (messaging, observability, internal SLA).
13. A row names functions, states, log fields, or dashboards.
14. There is more than one metrics table, or a Metric name needs a glossary.

**Requirements**
15. A capability has no job story, or the story restates the feature.
16. A situation is "when using X," or a "so they can" is something the system does.
17. A job-doer is an individual, or the system itself.
18. A capability is named after an implementation detail, or one workflow is split across fragments.
19. An acceptance paragraph exceeds three sentences, or the capability has no testable done condition.
20. A requirement prescribes classes, tables, jobs, or APIs.

**Language and references**
21. Codebase or ticket jargon appears in Problem, Success, or Requirements.
22. An individual is named outside Reviewers or Owner columns.
23. References contain local files, repo paths, or instruction files, or the doc has a meta footer.
24. An em dash, a `~` approximation, or a leftover italic instruction remains.
25. A claim contradicts the research bundle without an Open Question noting it.

**Engineer test (the floor)**
26. An engineer writing the tech spec would have to ask a product question the PRD does not answer: what happens in an edge case, what a term means, who decides, what the user sees on failure. Add the answer to the job's acceptance contract. Questions about how to build it (storage, services, queues) are engineering's call and are not violations.
27. A term an engineer could read two ways ("claim," "approved," "active") is used without being defined the first time it appears.
