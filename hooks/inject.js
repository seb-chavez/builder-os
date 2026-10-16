#!/usr/bin/env node
// SessionStart: Red Pen's rules plus the using-product-os skill list.
// SubagentStart: Red Pen's rules only; sub-agents get a narrow job and don't need the skill list.
const fs = require("fs");
const path = require("path");

let event = "SessionStart";
try {
  event = JSON.parse(fs.readFileSync(0, "utf8")).hook_event_name || event;
} catch {}

const root = path.join(__dirname, "..");
const read = (p) => fs.readFileSync(path.join(root, p), "utf8");
let context = read("rules/red-pen.md");
if (event === "SessionStart") {
  const skill = read("skills/using-product-os/SKILL.md").replace(/^---\n[\s\S]*?\n---\n/, "");
  context += `\n\n${skill}\nproduct-os is installed at ${root}. Paths like templates/ and rules/ are relative to it.\n`;
}
process.stdout.write(JSON.stringify({
  hookSpecificOutput: { hookEventName: event, additionalContext: context },
}));
