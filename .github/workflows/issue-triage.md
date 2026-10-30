---
description: |
  Triages each new issue: reads it and the code, adds one label,
  and leaves a short comment for the maintainer.

on:
  issues:
    types: [opened]
  reaction: eyes

permissions:
  contents: read
  issues: read
  copilot-requests: write

engine:
  id: copilot
  model: gpt-6-luna
  fallback-models: [gpt-5.6-luna, claude-haiku-4.5]

safe-outputs:
  add-labels:
    allowed: [bug, enhancement, question, documentation]
    max: 1
  add-comment:
    max: 1
  threat-detection:
    engine:
      id: copilot
      model: gpt-6-luna

timeout-minutes: 10
---

# Issue triage

Read issue #${{ github.event.issue.number }} and the code in this repository.

1. Decide what kind of issue it is: `bug`, `enhancement`, `question` or `documentation`.
   Add that one label.
2. If it is a bug, find the line in the code that causes it.
3. Leave one short comment (at most five sentences) in plain English:
   what the issue is, the file and line at fault, and a suggested fix.

Do not guess. If the issue does not give enough detail, say what is missing.
