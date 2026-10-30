# gh-aw-demo

A small public demo of **GitHub Agentic Workflows** (`gh aw`), made for a video on 30 October 2026.

- `cart.py` is a tiny shopping-cart script. It has one bug on purpose.
- `.github/workflows/issue-triage.md` is an agentic workflow written in Markdown.
  `gh aw compile` turns it into `.github/workflows/issue-triage.lock.yml`, a normal GitHub Actions workflow.
- When someone opens an issue, the workflow asks an AI agent (GitHub Copilot) to read the issue and the code,
  add one label and leave a short comment.

Run the script:

```
python3 cart.py
```
