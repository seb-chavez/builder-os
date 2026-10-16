---
name: prospecting
description: Use when finding, researching, verifying, or ranking business-development prospects, drafting outreach for the user to send, or following up on a prospect's reply. Triggers on "prospect", "find leads", "research this firm for outreach", "who should I reach out to", "draft outreach", "follow up on this reply".
---

# Prospecting

Business development. The output is verified prospect files and outreach drafts. The user reviews and sends every message; nothing is sent automatically, and LinkedIn is never automated (its user agreement bans scraping and automated messaging, and the user's own account is usually the main sales channel).

## First: the workspace profile

Everything specific to the business lives in the workspace's `prospecting.md`: what it sells, the segments it targets, fit criteria, who to contact at each kind of prospect, and the user's message rules. Read it before anything else.

If it is missing, stop. Offer to write it with the user from [profile-template.md](profile-template.md), one question per message. Never invent fit criteria, an offer, or message rules.

## The pipeline

1. **Brief (ask the user).** Before any search, ask (skip what they already said; use the harness's multiple-choice question tool if it has one):
   - **Segment** and **geography**, from the options in the profile.
   - **Signals to favor**, from the profile (multi-select).
   - **How many** to research this run (default 5; each takes about 15 minutes to research and verify).

   Save the answers to `accounts/_briefs/YYYY-MM-DD-<segment>.md`, with one line on which offer fits this segment.
2. **Propose a list (the user approves).** Check `accounts/_pipeline.md` and `accounts/` so nobody is researched or contacted twice. Do a light search for candidates that match the brief and show about twice as many as asked: name, one line on why, one source link each. Only the user's picks get researched.
3. **Research:** one `prospect-researcher` agent per approved prospect, in parallel. Give each the absolute paths of this file, the workspace's `prospecting.md`, and the prospect's folder.
4. **Verify:** one `claim-verifier` agent per prospect, after its research is done, with the same paths. Only prospects marked `Ready for outreach: yes` move on.
5. **Rank** the ready prospects (see Ranking) and show the list: one contact per prospect, the reason, the channel.
6. **Draft** messages for the ones the user picks (see Messages). Save each to `accounts/<slug>/YYYY-MM-DD-outreach.md`.
7. **Track.** When the user says a message went out, add or update its row in `accounts/_pipeline.md`: who, when, channel, status, next step.

## Evidence rules

Outreach goes out under the user's name, so a wrong fact is worse than a missing one.

- **Official sources only for facts that drive a decision:** the prospect's own site, its portfolio companies' own sites, the firm's own team and portfolio pages, official press releases, or a partner's official page about the company. Data brokers, job boards, review sites, and search snippets can point you somewhere; they are never the evidence.
- **Quote, don't paraphrase.** Every fit carries a short verbatim quote and its URL.
- **Claim only what the quote says.** Most research errors are overreach, not invention: a 2023 board seat stated as current, a fund still raising given a final size, a product feature read more broadly than the page says. State what the source shows, with its date, and mark the rest `likely` or `unverified`. Fund sizes only from the firm's own announcement of a final close.
- **WebFetch summarizes and can mislabel.** Ask it to quote verbatim. For anything a recommendation rests on (a category tag, a team listing, a board seat), confirm with the raw HTML via curl. If a page renders with JavaScript and comes back empty, read its HTML or JS bundle.
- **Deal teams come from the firm's own portfolio-company pages.** A press-release quote shows who spoke, not who sits on the board.
- **Check status.** Firm sites often list sold companies as active. Search for an exit before calling a company current.
- **Emails only if published** on an official page, quoted with the source. Never guess a pattern. Otherwise write `not public` and plan for LinkedIn.

## Confidence levels

| Level | Meaning |
|---|---|
| `confirmed` | Verbatim on an official page, checked directly |
| `likely` | Official source, but indirect (a firm's description of its company, an undated page) |
| `unverified` | Third-party source only, or could not be checked |
| `unknown` | No evidence either way |

A fit can be rated **high** only on `confirmed` evidence. No evidence means fit `unknown`, not low and not high.

## Ranking

Unless the profile says otherwise, rank ready prospects by: (1) how many confirmed high fits, (2) whether the contact's job matches the offer, (3) reachability (published email, nearby, shared network), (4) timing signals (new fund, recent deal, launch, rebrand).

## Files

Folder: `accounts/<slug>/` (lowercase, hyphenated company name).

- `account.md`: from the workspace's account template if it has one. Contacts table with role, relevant companies with source, and email (`not public` if not published). Notes start with who to contact first and why.
- Investment firms only: `YYYY-MM-DD-portfolio-screen.md` from [portfolio-screen.md](portfolio-screen.md).
- `YYYY-MM-DD-verification.md`: written by the verifier.
- `YYYY-MM-DD-outreach.md`: the drafted messages.

Plain language: the reader is an operator or investor, not a specialist.

## Messages

Follow the profile's message rules. On top of them, always:

- **One public, confirmed fact explaining why this person:** a board seat, a deal, a role, a launch. Never imply the user has analyzed their company.
- **LinkedIn connection notes: 300 characters maximum, counted with code.** Ask to connect only; the offer goes in the follow-up after they accept.
- **Emails only to published addresses.**
- **Follow-up after a LinkedIn accept:** thank them, one line on their specific company or initiative, then the offer. Use their reply's context if there is one.

## After a reply

Read the reply, update `accounts/_pipeline.md`, and draft a response that moves toward the profile's next step (a call, a meeting). If they asked for something specific, answer that first.
