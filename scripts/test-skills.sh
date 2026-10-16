#!/usr/bin/env bash
# Runs each skill's test cases (skills/<name>/evals/) with `claude plugin eval`,
# with and without the skill, and prints one summary line per skill.
#
# Usage:
#   ./scripts/test-skills.sh                  # every skill that has cases
#   ./scripts/test-skills.sh product-brainstorming meeting-prep
#   RUNS=1 ./scripts/test-skills.sh ...       # quicker, noisier (default 3 runs per case)
#
# Every run calls a model and bills your Claude plan. Run a skill's cases after
# changing that skill, and the full set before larger changes. CI does not run these.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
RUNS="${RUNS:-3}"
MODEL="${MODEL:-sonnet}"
CONCURRENCY="${CONCURRENCY:-2}"
TMP_ROOT="${TMPDIR:-/tmp}"
OUT="$(mktemp -d "${TMP_ROOT%/}/test-skills.XXXXXX")"
trap 'rm -rf "$OUT"' EXIT

if [ "$#" -gt 0 ]; then
  names=("$@")
else
  names=()
  for dir in "$REPO"/skills/*/evals/; do
    names+=("$(basename "$(dirname "$dir")")")
  done
fi

failed=0
for name in "${names[@]}"; do
  dir="$REPO/skills/$name"
  [ -d "$dir/evals" ] || { echo "SKIP  $name (no evals/)"; continue; }
  echo "RUN   $name"
  if ! (cd "$dir" && claude plugin eval . --runs "$RUNS" --model "$MODEL" --concurrency "$CONCURRENCY" \
        --no-publish --trust-plugin --threshold 0 --json "$OUT/$name.json" >/dev/null); then
    echo "ERROR $name (see skills/$name/evals/results/)"
    failed=1
    continue
  fi
  python3 - "$OUT/$name.json" "$name" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
weak = [f"{c['name']} ({c['aggregates']['score']:.2f})" for c in d["cases"] if c["aggregates"]["score"] < 1]
a = d["aggregates"]
print(f"      {sys.argv[2]}: {a['casesPassed']}/{a['casesTotal']} cases pass, "
      f"score {a['overallScore']:.2f}, with-vs-without delta {a.get('meanDelta') or 0:+.2f}, ${d['costUsd']:.2f}")
for w in weak:
    print(f"      below 1.0: {w}")
PY
done
exit "$failed"
