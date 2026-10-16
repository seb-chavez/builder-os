# product-os

*Skills for product and consulting work, with an editor's red pen built in.*

PMs and consultants drafting with an AI agent hit the same problems: the agent jumps to solutions before the problem is framed, writes PRDs that leave engineers guessing, and pads every doc until it reads like AI wrote it. product-os is one Claude Code plugin with a skill for each step, from brainstorming to a reviewed PRD, plus Red Pen's writing rules on in every session.

## Skills

| Skill | Use when |
| ----- | -------- |
| `product-brainstorming` | A problem or idea needs exploring before anything is written, solo or as a team workshop |
| `product-researching` | A problem needs investigating before a PRD (`/product-researching`) |
| `product-requirements-drafting` | Writing or updating a PRD, with a fresh reviewer pass against the PRD rulebook |
| `review-panel` | A doc needs one reviewer persona or a panel: pessimist, optimist, operator, new hire, budget, engineer, executive, champion user |
| `meeting-prep` | Preparing for a meeting, from the workspace's notes |
| `new-workspace` | Starting a new client, employer, or project |
| `red-pen` | A draft is too long or reads like AI wrote it |
| `writing-skills` | Creating or editing a product-os skill |

A session-start hook loads Red Pen's rules and a short skill list (`using-product-os`), the same pattern as [Superpowers](https://github.com/obra/superpowers). Every other skill loads only when a request matches it, so the plugin stays quiet in repos where you are writing code. Document templates (agenda, decision log, project brief, status update, roadmap, discovery questions, PRD) live in [templates/](templates/).

## Workspaces

Notes about people and projects live in a **workspace**: one private repo per boundary of context (an employer, a client, a standalone effort), with an `AGENTS.md` and a `canonical/` folder. `/new-workspace` sets one up. Skills read only the current workspace, so one client's notes never show up in another's meeting prep. Outside a workspace, the skills ask you for context instead.

## Red Pen

Red Pen holds each doc type to a length budget, and it never cuts the detail engineers need to build from.

| Plugin | For | What it cuts |
| ------ | --- | ------------ |
| [Caveman](https://github.com/JuliusBrussee/caveman) | Anyone using an agent | How the agent talks to you |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Engineers | How much code gets written |
| **Red Pen** | PMs and founders | How long your shared docs get, without cutting what engineers need |

### Why

The obvious fix, "be concise," breaks specs: a PRD trimmed for word count leaves engineers guessing, and guessing ships the wrong thing. So Red Pen gives each doc type a **ceiling** and a **floor**:

| Doc type | Ceiling | Floor |
| -------- | ------- | ----- |
| Strategy, founder brief | One page; mission in one sentence | The bet, who pays, proof, biggest risk, kill condition |
| Status update | 150 words | What changed, what is blocked, what you need |
| PRD requirements | None | Every trigger, branch, limit, and term an engineer needs |
| Slack | 1 to 3 sentences | The ask or the answer |

When they conflict, the floor wins. Full rules: [rules/red-pen.md](rules/red-pen.md).

### Results

Five fictional PM docs, each written from notes and edited from a bloated draft. Sonnet, 3 runs per cell, median. Same docs, same prompts, three arms. [Full report](eval/results/2026-10-04-sonnet.md).

| | No skill | Caveman | **Red Pen** |
| - | --: | --: | --: |
| Strategy doc, written from notes (words) | 821 | 607 | **251** |
| Status update, edited (words) | 178 | 134 | **85** |
| Facts kept (numbers, dates, decisions) | 99% | 99% | **99%** |
| AI tells per doc (em dashes, "pivotal," "in conclusion") | 0.3 | 0.1 | **0.0** |
| PRD behaviors **wrong or missing**, edited from a thin draft (of 7) | 2.0 | 1.0 | **0.0** |

That last row is the one other tools can't claim. The draft PRD left several behaviors unspecified. With no skill, the model filled them in with plausible, wrong answers ("reply R adds the patient to the waitlist"; the real spec sends a link to rebook). Red Pen wrote **Open question** instead. A confident wrong spec is worse than an honest gap.

When it wrote PRDs from complete notes, every arm got all 7 behaviors right. Red Pen just used fewer words.

### Before and after

A 696-word founder brief ("In today's rapidly evolving healthcare landscape...") became:

> **The bet:** Owner-run practices with 3 to 15 dentists will pay a flat $399 a month to cut no-shows, if setup takes a day instead of six weeks.
>
> ...
>
> **Proof so far:** 61 clinics served. $1.2M annual recurring revenue [check: 61 clinics at $399 a month is about $0.29M a year. Confirm the pricing, the ARR, or whether other plans exist].

305 words, every number and the kill condition kept. It also caught an arithmetic error we had planted in the test draft by accident.

## Install

**Claude Code:**

```
/plugin marketplace add seb-chavez/product-os
/plugin install product-os@product-os
```

Or turn it on for one repo only, in `.claude/settings.json` (or `.claude/settings.local.json` to keep it off a shared repo):

```json
{
  "extraKnownMarketplaces": {
    "product-os": { "source": { "source": "github", "repo": "seb-chavez/product-os" } }
  },
  "enabledPlugins": { "product-os@product-os": true }
}
```

**Cursor, Codex, or any agent that reads `AGENTS.md`:** paste [rules/red-pen.md](rules/red-pen.md) into your `AGENTS.md` or rules file. The skills are plain `SKILL.md` folders and work in any harness that reads them.

## Use

Red Pen is on from the first message, in the main session and every sub-agent. To edit an existing draft:

```
/red-pen path/to/draft.md          # full: returns the edited draft
/red-pen path/to/draft.md lite     # lists cuts, changes nothing
/red-pen path/to/draft.md ultra    # also asks whether the doc should exist
```

Every edit reports `Words: before → after`, what was cut, what moved behind links, and what was kept or added on purpose. Say "red pen off" to stop.

## How it is measured

- **On every PR (free):** `python -m unittest discover -s tests` checks the scoring code, the test docs, the manifests, the hook, skill frontmatter, skill lists, links, and em dashes. No model calls.
- **Skill cases (by hand):** `./scripts/test-skills.sh <skill>` runs each skill's cases in `skills/<name>/evals/` with and without the skill, through `claude plugin eval`. Bills your Claude plan.
- **Before a release (maintainer, by hand):** `python3 eval/bench.py --model sonnet --repeats 3`. Runs through the `claude` CLI in `--safe-mode`, so it bills to your Claude plan, needs no API key, and ignores your personal setup. Results land in [eval/results/](eval/results/) with every raw output.

Words, facts kept, and AI tells are counted by code. PRD behaviors are scored by a judge model against the true intended answer for each one.

**Limits:** five docs, one model, three runs per cell. The test docs are fictional and written by the author. Treat the numbers as directional, and rerun them on your own docs.

## License

MIT. The ladder pattern is inspired by [Ponytail](https://github.com/DietrichGebert/ponytail); the comparison arm uses [Caveman](https://github.com/JuliusBrussee/caveman)'s skill, fetched at run time.
