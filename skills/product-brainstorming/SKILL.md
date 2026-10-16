---
name: product-brainstorming
description: Use when a product idea, feature request, or problem needs brainstorming before anything gets written, solo or as a team workshop. Triggers on "brainstorm", "ideation session", "run a workshop", "how might we", "crazy eights", "reverse brainstorm".
---

# Product Brainstorming

Go wide, then narrow. Five steps, in order: **frame, pick a method, diverge, converge, hand off.** Framing comes first because ideas aimed at the wrong problem are wasted. Judging comes last because judging early kills ideas before they exist.

## When NOT to use

- A sizing or feasibility question ("how many customers hit this?"). Answer it directly, or run `product-researching`
- The problem and the solution are already agreed and you want the document. That is `product-requirements-drafting`
- Reviewing something already written. That is `review-panel`

## Step 0: Solo or workshop?

Ask once, in your first message: **"Solo session with me, or are we prepping a workshop for your team?"**

| Mode | Who generates ideas | What the agent does |
| ---- | ------------------- | ------------------- |
| **Solo** | The PM and the agent, live in chat | Runs each round, asks for the PM's ideas first, then adds its own |
| **Workshop** | The PM's team, in a room or on a board | Builds the facilitator kit, then runs steps 4 and 5 on the team's output |

## Step 1: Frame the problem

1. Read the current state, if this is a workspace: `canonical/projects/`, related people files, `canonical/GOALS.md`.
2. Ask up to three questions, **one per message**: who has the problem, what outcome would show it is solved, and what constraints are fixed (time, team, platform).
3. Write the frame:
   - **How might we** [one question, aimed at the outcome, not a solution]?
   - **For:** who has the problem.
   - **We'll know it worked when:** one observable outcome.
   - **Fixed constraints:** only the real ones.
4. **Stop and get a yes.** Do not pick a method until the frame is approved.

If the PM arrives with a solution ("we need a dashboard"), first ask what problem it solves. That question comes before the three above and does not count toward them. Remember the anchoring, and in step 2 recommend a reverse brainstorm because of it.

## Step 2: Pick a method

Recommend one method with a one-line reason, then let the PM choose. Full steps for each are in [references/methods.md](references/methods.md); read only the one you are running.

| Situation | Method |
| --------- | ------ |
| The team is anchored on a solution that is already written up | Reverse brainstorm |
| The outcome is known, and there are many possible ways to get there | Opportunity solution tree |
| You need a lot of different ideas fast | Crazy Eights |
| You are improving something that already exists | SCAMPER |
| A new product or flow from start to finish | User story map |
| Ideas must tie back to a business goal | Impact mapping |

## Step 3: Diverge

**Solo:**
- Run the method one step at a time. Each round, ask for the PM's ideas **before** offering yours, so yours do not anchor theirs. Label yours as the agent's.
- Quantity over quality: aim for 15 to 30 ideas across the session. No scoring, no "but" during this step.
- Push past the obvious. After the first easy round, ask for the weird version, the version for a different user, the version with no budget.

**Workshop:** write the facilitator kit to `canonical/projects/<project>/workshops/YYYY-MM-DD-<method>.md`:
- The approved frame, to put at the top of the board.
- An agenda with timings (most methods fit in 45 to 60 minutes).
- The exact prompt for each round, word for word.
- What to prepare (board template, sticky colors, who facilitates, who keeps time).
- What to capture at the end, so step 4 can run on it.

Then stop. When the PM brings back the team's output (pasted, a photo, a board export), continue at step 4.

## Step 4: Converge

1. **Cluster:** merge duplicates and group the ideas into themes. Show the themes with their ideas underneath.
2. **Score** each theme in one table:

   | Theme | Impact on the outcome | Effort (S / M / L) | Confidence | Riskiest assumption |
   | ----- | --------------------- | ------------------ | ---------- | ------------------- |

3. **Recommend one or two**, with the reason in a sentence. Optional: run Six Thinking Hats on the leader (in `references/methods.md`) to pressure-test it.
4. **Stop and let the PM pick.** Keep the runners-up as a one-line list; they are the alternatives the brief will mention.

## Step 5: Write it up and hand off

Write the brief with [templates/strategy/project-brief.md](../../templates/strategy/project-brief.md), saved to `canonical/projects/<project>/`. It records: the frame, the chosen idea, the alternatives considered and why they lost, and the riskiest assumptions. Apply Red Pen budgets: a brief is one page.

Hand off to `product-researching`. The riskiest assumptions become its research questions. Do not draft a PRD from here.

## Common mistakes

| Mistake | Fix |
| ------- | --- |
| Generating ideas before the frame is approved | Step 1 ends with a yes. No yes, no method |
| Offering the agent's ideas first | The PM goes first every round; the agent's ideas anchor everyone who sees them |
| Scoring during diverge | Divergence has no judging. Hold every "but" for step 4 |
| Stopping at ten obvious ideas | Push for the weird version, a different user, no budget |
| Asking several questions in one message | One per message; batched questions get one merged answer |
| Skipping converge and picking a favorite | Cluster and score in the table, then let the PM pick |
| Workshop kit without exact prompts | Write each round's prompt word for word; the facilitator reads it out |
| Jumping from the winner to a PRD | The winner goes to `product-researching` first |

## Attribution

Step 1's approval gate is adapted from `superpowers:brainstorming` by Jesse Vincent, MIT licensed. Methods are credited in `references/methods.md`.
