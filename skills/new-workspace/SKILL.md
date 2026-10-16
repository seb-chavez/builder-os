---
name: new-workspace
description: Use when starting work with a new client, a new employer, or a big standalone effort, or when adding a new project to an existing workspace. Triggers on "new client", "new workspace", "set up a workspace", "starting a new project", "new engagement".
argument-hint: "[name]"
---

# New Workspace

## Overview

Sets up either a new workspace (its own private repo) or a new project folder inside the current one. Same layout for product and consulting work. Layout and rules are in `using-builder-os`.

## Steps

1. **Workspace or project?** Ask once, unless the request already says:
   - **New workspace:** a new boundary for context. A new client, a new employer, a big standalone effort. Nothing in it should ever mix with another workspace.
   - **New project:** another piece of work inside the current workspace (a second engagement with the same client, a new initiative at the same job).

   If you are not inside a workspace (no `canonical/` here), it can only be a new workspace.

### New project

2. Ask for a short project name. Create `canonical/projects/<slug>/` with one note, `YYYY-MM-DD-kickoff.md`, holding what the user told you about the project. Stop.

### New workspace

2. Ask, one per message, only what you do not already know:
   - The name (becomes the folder and repo name, kebab-case).
   - What it is: employer, client, or standalone. For a client: the client's name, and what is confidential.
   - Where docs publish (Notion, Google Docs, local only) and which work tools are reachable (chat, tracker, data).
3. **Confirm before writing:** the folder path (default `~/<name>`), and the files below. Wait for a yes.
4. Create:
   - `AGENTS.md` from [workspace-agents.md](workspace-agents.md), every bracket filled from the answers. Delete lines with no answer rather than leaving brackets.
   - `CLAUDE.md` containing one line: `@AGENTS.md`.
   - `.claude/settings.json` turning on builder-os:
     ```json
     {
       "extraKnownMarketplaces": {
         "builder-os": { "source": { "source": "github", "repo": "seb-chavez/builder-os" } }
       },
       "enabledPlugins": { "builder-os@builder-os": true }
     }
     ```
   - `canonical/people/`, `canonical/projects/`, `canonical/company/`, `canonical/teams/`, each with a `.gitkeep`, and an empty `canonical/GOALS.md`.
5. `git init` and make the first commit. `canonical/` **is** committed: this repo is private, and git is its backup.
6. **Do not create a remote or push.** Ask where it should live. A client's notes on a personal GitHub account can break a client agreement; the user decides.
7. Tell the user to open a new session in the folder so the workspace loads.

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Creating a project folder inside the wrong workspace | Check which workspace you are in before writing |
| Copying people or notes from another workspace to "seed" this one | Never. Each workspace starts empty |
| Gitignoring `canonical/` | It is the point of the repo. Keep the repo private instead |
| Pushing to GitHub without asking | Ask first. Where client data lives is the user's call |
