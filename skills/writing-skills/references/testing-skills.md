# Testing Skills

**Load this when:** writing or editing a skill that enforces a discipline, before you rely on it.

## Overview

Testing a skill is the same loop as testing anything else. You run the scenario without the skill and watch it fail, you write the skill against those specific failures, then you close the loopholes that show up next.

**Core principle: if you did not watch it fail without the skill, you do not know whether the skill prevents the right failure.**

## What needs testing

Test skills that:

- Enforce a discipline (a rule with a cost to following it)
- Can be rationalized away in the moment
- Cut against what you want to do right then (thoroughness against a deadline)

Do not bother testing:

- Pure reference skills
- Skills with no rule to violate
- Skills nobody has an incentive to bypass

For those, the check is simpler: can someone find the information and use it correctly?

## Phase 1: Baseline. Watch it fail

Run the scenario with the skill absent. Document what happened word for word.

For a discipline skill, an academic prompt tells you nothing. "What does good PRD writing look like?" gets you a recitation. You need a scenario with pressure where the wrong choice is genuinely attractive.

**A weak scenario:**

> You are writing the Problem section of a PRD. What do you do?

Too academic. It just recites the rule back.

**A strong scenario:**

> You have been asked for the inbound credits PRD by end of day. You have already agreed the fix with engineering: read every name field on the entry, then fall back to fuzzy matching. The exec asking for it wants to see the approach, not a problem statement. You have 40 minutes.
>
> A) Write the Problem section with no solution in it, then the Proposal
> B) Lead with the matching change so the exec sees the approach immediately
> C) Put a short version of the solution in Problem for context, expand it in Proposal
>
> Choose A, B, or C. Be honest about which you would actually do.

Time pressure, plus authority, plus the fact that the answer is already known. That combination is what surfaces the real rationalizations.

### Pressure types

| Pressure | Example |
|---|---|
| Time | Deadline today, meeting in an hour |
| Sunk cost | Already drafted it the other way |
| Authority | An exec or a senior stakeholder asked for it differently |
| Social | Looking rigid or process-bound in front of the team |
| Exhaustion | End of the day, third doc this week |
| Pragmatic | "Being practical rather than dogmatic" |

**The useful tests combine three or more.**

### What makes a scenario work

1. **Concrete options.** Force a choice between A, B, and C rather than leaving it open
2. **Real constraints.** Specific times, named stakeholders, actual consequences
3. **Real artifacts.** Point at a document that exists, not "a doc"
4. **Ask what you would do,** not what you should do
5. **No easy out.** Do not leave "I would ask the user" available as a way to dodge the choice

Write down the rationalizations verbatim. They are the raw material for the skill.

## Phase 2: Write against what you saw

Address the specific failures you documented. Nothing else. Content written for hypothetical failures is content nobody needed.

Run the same scenario with the skill present. If it still fails, the skill is unclear or incomplete, not the reader.

## Phase 3: Close the loopholes

A skill that gets followed once is not finished. Each new rationalization gets four things:

**1. An explicit negation.** Not just the rule, but the specific workaround forbidden by name.

Before:

> Do not solution in the Problem section.

After:

> Do not solution in the Problem section.
>
> No exceptions:
> - Not "brief context on the approach"
> - Not "a sentence so the reader understands the shape"
> - Not naming the solution while describing the problem it solves
> - If the reader needs the solution to understand the problem, the problem is not written yet

**2. A row in the rationalization table.**

| Excuse | Reality |
|---|---|
| "One line of context so the exec follows it" | That line is the whole solution. Move it to Proposal |

**3. A red flag entry**, so the reader catches themselves mid-argument.

**4. A description update**, adding the symptom of being about to violate the rule.

Then re-run the scenario. If a new rationalization appears, repeat. If the rule holds, it is done for that scenario.

## Meta-testing when it will not go green

When it reads the skill and still picks the wrong option, ask directly:

> You read the skill and chose C anyway. How should that skill have been written so A was clearly the only acceptable answer?

Three answers, three different fixes:

| Answer | Problem | Fix |
|---|---|---|
| "It was clear, I chose to ignore it" | Not a documentation problem | Add the foundational principle: violating the letter is violating the spirit |
| "It should have said X" | Documentation gap | Add X, in their words |
| "I did not see that section" | Organization | Move the key point earlier and make it prominent |

## Knowing when it is done

Done looks like:

- The correct option gets chosen under maximum pressure
- The skill's own sections get cited as the reason
- The temptation is acknowledged, and the rule is followed anyway

Not done if:

- New rationalizations keep appearing
- The skill itself gets argued with
- Hybrid approaches get invented to split the difference
- Permission is requested, with a strong argument for the violation attached

## A note on running these

Baseline and pressure tests need a fresh context that has not seen the conversation where you designed the skill. In Claude Code that means a subagent or a separate session. Running the scenario on yourself, in the session where you just wrote the skill, proves nothing: you already know the answer you are looking for.

For most PM workflow skills you do not need any of this. Run the skill on a real document you have already revised and compare the output to the version you shipped. That is a sufficient test for anything that is not enforcing a rule.

## Attribution

Adapted from `superpowers:writing-skills` by Jesse Vincent, MIT licensed. The RED-GREEN-REFACTOR framing is inlined here rather than depending on a separate test-driven-development skill, and the examples are PM work rather than code.
