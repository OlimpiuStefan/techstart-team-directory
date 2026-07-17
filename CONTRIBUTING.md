# How we work

The rules we all follow, so 12 people can write in the same code without stepping on each other.

At work, this file is the first thing you read when you join a project.

## Branches

| Branch | What it is | Who writes here |
|--------|-----------|-----------------|
| `main` | the code that would run in production | **nobody directly.** Only a pull request from `develop`, approved by the trainer. |
| `develop` | where everyone's work comes together | only a pull request from `feature/*`, with 1 approval |
| `feature/*` | your work | you, freely |

**Never work directly on `main` or `develop`.** The server will refuse you anyway.

## Branch names

```
feature/<your-name>-<short-description>
```

✅ `feature/maria-add-profile`
✅ `feature/alice-readme-team-table`
❌ `fix`, `test`, `maria`, `branch2`, `asdf`

In three months, someone looks at the branch list. The name has to say what it was for.

## Commit messages

```
type: what it does
```

| Type | When |
|------|------|
| `feat` | new feature |
| `fix` | bug fix |
| `docs` | documentation |
| `chore` | everything else |

✅ `feat: add Maria Ionescu profile`
✅ `fix: handle profiles with no role field`
❌ `update`, `fix`, `wip`, `changes`, `final2`

> **The message says WHY, not WHAT.** What you did is in the diff. Why you did it is nowhere else.
> In six months, you are the one reading it, at 2am, when something is broken.

## Pull requests

- **One pull request, one idea.** If your description needs the word "and", it's probably two.
- Title in the same format as a commit message.
- Fill in the description: what, why, how you tested.
- Assign a reviewer.

## Reviews

1. **"LGTM" is not a review.** Leave at least one real comment on a line of code.
2. **Comment on the code, not the person.**
3. **Do not approve what you did not read.** If you don't understand it, ask in the pull request. That is your job as a reviewer.
4. **If you request changes, say exactly what needs to change** for you to approve.

## Merging

The LM tutorial says either **Squash and merge** or **Merge commit** is fine for a feature.
Our team convention:

| From | To | How | Why |
|------|----|-----|-----|
| `feature/*` | `develop` | **Squash and merge** (preferred) | Clean history: one commit per feature. Merge commit is also OK. |
| `develop` | `main` | **Merge commit** | You can see what went into each release. |

**The author merges, not the reviewer.** You wrote it, you finish it.
**Delete your feature branch after merging** — the repo does this automatically.

## Never commit

Passwords · API keys · tokens · `.env` files · `node_modules/` · big files

> ⚠️ Once a key is in a commit, it stays in the history **forever**, even if you delete the file in the next commit.
> That is a security incident, not a coding mistake. **If it happens, say so immediately.** The key has to be replaced.

## Keeping your branch fresh, and fixing conflicts

Merge `develop` into your branch regularly — daily, if your branch lives that long.

```bash
git checkout develop
git pull origin develop
git checkout feature/your-branch
git merge develop
# if there's a conflict: fix the <<<<<<< ======= >>>>>>> markers in your editor
git add <file>
git commit
git push
```

A conflict is not an error. Git cannot guess whether your line goes above or below your colleague's. It's asking you.

Lost? **`git merge --abort`** puts you back exactly where you started. Nothing is lost.

*(The slides show `git rebase develop` instead — a cleaner, straight history, but it rewrites your commits and needs a force-push. Either works; we use merge because it's simpler and safer.)*
