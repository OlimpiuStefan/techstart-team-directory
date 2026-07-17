# TechStart Team Directory

A small app for the Git training. Everyone adds their profile. The app lists them.

## Run it

```bash
python3 src/app.py
```

## How to contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Short version:

1. Start from `develop`, up to date
2. `git checkout -b feature/<your-name>-<description>`
3. Make your change, commit, push
4. Open a pull request into `develop`
5. A colleague reviews it, you merge it

**Never push straight to `main` or `develop`.** It won't let you anyway.

The team roster is in **[TEAM.md](TEAM.md)** — that's where Round 2 happens.

---

## What's in here

```
TEAM.md          the shared team table  ← round 2 (everyone edits it = conflict)
profiles/        one .md file per person  ← round 1 (no conflicts)
  _template.md   copy this to make yours
src/app.py       reads the profiles and lists them
CONTRIBUTING.md  the team's rules
```
