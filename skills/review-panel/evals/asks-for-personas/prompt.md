---
name: asks-for-personas
tags: [slash, behavior]
max_turns: 3
allowed_tools: [Skill, Read, Glob, Grep]
---

/review-panel

Review this PRD, pasted below.

# PRD: SMS appointment confirmations for Tidewell clinics

## Problem
Patients miss 12% of appointments. Front desks call each patient the day before, which takes about 90 minutes a day per clinic.

## Proposal
Send an SMS 24 hours before each appointment. Patients reply C to confirm or R to reschedule.

## Plan
Pilot at 12 clinics in November, then roll out to all 140.
