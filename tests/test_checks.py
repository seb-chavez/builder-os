"""Free checks for CI: scoring logic and fixture validity. No model calls."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "eval"))
import checks  # noqa: E402

FIXTURES = ROOT / "eval" / "fixtures"


class Checks(unittest.TestCase):
    def test_words(self):
        self.assertEqual(checks.words("one two  three\nfour"), 4)

    def test_tells(self):
        t = checks.tells("This is a pivotal moment — it's not just software, it's a movement.\nIn conclusion, wow.")
        self.assertEqual(t["em_dash"], 1)
        self.assertEqual(t["ai_vocabulary"], 1)
        self.assertEqual(t["contrast_setup"], 1)
        self.assertEqual(t["summary_ending"], 1)

    def test_clean_text_has_no_tells(self):
        self.assertEqual(checks.tells("Launch slips to May 12. Legal must sign the consent text by Wednesday.")["total"], 0)

    def test_facts_kept(self):
        self.assertEqual(checks.facts_kept("ARR is $1.2M", [r"\$1\.2 ?M", "ChairSync"])[:2], (1, 2))


class Fixtures(unittest.TestCase):
    def test_every_fixture_holds_its_facts(self):
        dirs = [d for d in FIXTURES.iterdir() if d.is_dir()]
        self.assertEqual(len(dirs), 5)
        for d in dirs:
            meta = json.loads((d / "meta.json").read_text())
            for name in ("notes.md", "draft.md"):
                kept, total, missing = checks.facts_kept((d / name).read_text(), meta["must_keep"])
                self.assertEqual(kept, total, f"{d.name}/{name} is missing {missing}")

    def test_drafts_are_bloated(self):
        # The edit-mode drafts must carry tells, or there is nothing to measure.
        for d in FIXTURES.iterdir():
            if d.is_dir():
                self.assertGreater(checks.tells((d / "draft.md").read_text())["total"], 0, d.name)


class Plugin(unittest.TestCase):
    def test_manifests_parse(self):
        for f in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "hooks/hooks.json"):
            json.loads((ROOT / f).read_text())

    def test_hook_injects_rules(self):
        for event in ("SessionStart", "SubagentStart"):
            out = subprocess.run(["node", str(ROOT / "hooks" / "inject.js")], input=json.dumps({"hook_event_name": event}),
                                 capture_output=True, text=True, check=True).stdout
            payload = json.loads(out)["hookSpecificOutput"]
            self.assertEqual(payload["hookEventName"], event)
            self.assertIn("The engineer test", payload["additionalContext"])
            # Only the main session gets the skill list.
            self.assertEqual("# Using builder-os" in payload["additionalContext"], event == "SessionStart")


SKILLS = ROOT / "skills"


class Skills(unittest.TestCase):
    def test_frontmatter_parses(self):
        # A broken frontmatter stops a skill loading, with no error a user would see.
        try:
            import yaml
        except ImportError:
            self.skipTest("pyyaml not installed; CI installs it")
        for f in SKILLS.glob("*/SKILL.md"):
            meta = yaml.safe_load(f.read_text().split("---")[1])
            self.assertEqual(meta["name"], f.parent.name)
            self.assertTrue(meta["description"], f)

    def test_skill_lists_agree(self):
        # using-builder-os tells the agent what exists; README tells people. Both must list every skill.
        names = {d.name for d in SKILLS.iterdir() if (d / "SKILL.md").exists()} - {"using-builder-os"}
        for doc in (SKILLS / "using-builder-os" / "SKILL.md", ROOT / "README.md"):
            text = doc.read_text()
            self.assertEqual({n for n in names if f"`{n}`" not in text}, set(), doc.name)

    def test_linked_files_exist(self):
        import re
        for f in list(SKILLS.rglob("*.md")) + [SKILLS / "using-builder-os" / "SKILL.md"]:
            for target in re.findall(r"\]\(((?:\.\./|[\w-]+/)[^)#]+\.md)\)", f.read_text()):
                self.assertTrue((f.parent / target).exists(), f"{f.relative_to(ROOT)} links missing {target}")
        for t in re.findall(r"`(templates/[\w/-]+\.md)`", (SKILLS / "using-builder-os" / "SKILL.md").read_text()):
            self.assertTrue((ROOT / t).exists(), t)

    def test_no_em_dashes(self):
        # Em dashes read as machine-written text. Fixtures are exempt: they are bloated on purpose.
        for f in ROOT.rglob("*.md"):
            if "eval" not in f.relative_to(ROOT).parts[0] and ".git" not in f.parts:
                self.assertNotIn("\u2014", f.read_text(), f.relative_to(ROOT))


if __name__ == "__main__":
    unittest.main()
