---
type: llm
---

PASS if, before drafting a SKILL.md, the reply asks for a past failure, a previous output that needed fixing, or a cold run of the task to write the skill against. Asking about the failure is required; it is what this skill teaches.
FAIL if the reply only asks generic setup questions (where the source material comes from, what format to use, who the audience is) without asking what went wrong before, or if it drafts a finished SKILL.md first, or if it stalls on not finding the repo without asking the failure question.
