# Git Training — Everything You Do Today

Your one-page-per-part handbook. Every command, and what it does. Follow along with the trainer.

> **Golden rule:** when you don't know what's happening, run **`git status`**. Git tells you what to do — you just read it.
> **When git asks for a password:** paste your **token**, not your account password. Nothing shows on screen — that's normal.

---

# Part 1 · Setup — get git working

### Check git exists
```bash
git --version              # should print: git version 2.x
```

### Tell git who you are (once, forever)
```bash
git config --global user.name "First Last"
git config --global user.email "first.last@libertymutual.com"
git config --global --list                       # check it took
```

### Point git at VS Code (so you never get trapped in vim)
```bash
git config --global core.editor "code --wait"    # opens VS Code for commit messages, waits for you to close it
git config --global alias.lg "log --oneline --graph --decorate --all"   # a nice history view
```
On **Windows only**:
```bash
git config --global core.autocrlf true            # stops every file looking "changed"
```

> `code: command not found`? In VS Code: `Cmd/Ctrl+Shift+P` → **Shell Command: Install 'code' command in PATH** → reopen the terminal.

### Make your token (the login for the terminal)
GitHub → profile picture → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)** → Note: `training`, Expiration: 30 days, Scope: tick **`repo`** → **Generate** → **copy it now** (you never see it again).

So you don't retype it every push:
```bash
# Mac:
git config --global credential.helper osxkeychain
# Linux:
git config --global credential.helper "cache --timeout=28800"
# Windows: already set up, do nothing
```

---

# Part 2 · Your first repo — the basics (on YOUR OWN repo)

Here your push **works** — it's yours, nothing is locked.

### Make your own practice repo
github.com → **`+`** → **New repository** → name `git-practice` → **Public** → ✅ **Add a README** → **Create**.
Then green **Code** button → **HTTPS** → copy the URL, and:
```bash
cd ~
git clone https://github.com/<your-username>/git-practice.git   # download it (first token prompt here)
cd git-practice
git status                 # On branch main, nothing to commit
ls -la                     # see the .git folder — THAT is the repo
```

### The daily loop: status → change → stage → commit → push
```bash
git status                 # where am I? what changed?
# edit README.md, add a line, save

git diff                   # what changed inside the file (green = added, red = removed)

git add README.md          # put the change in "the box" (the staging area)
git status                 # now green: "to be committed"
git diff                   # empty! (the change is in the box now)
git diff --staged          # this shows what's IN the box

git commit -m "docs: add my first line"   # seal the box with a message
git log --oneline          # see your commit
git show HEAD              # what the last commit changed  (HEAD = "you are here")

git push origin main       # send it to GitHub — IT WORKS (your repo). Refresh the page to see it.
```

### Pull — get changes from the server
```bash
git pull                   # fetch what's new on the server + merge it into what you have
```

| | What it is |
|---|---|
| `main` | **your** branch, on your machine |
| `origin/main` | your copy of the server, from your last fetch |
| `main` on GitHub | what's on the server **right now** |

### Never commit secrets
Passwords, API keys, `.env` files — never. A committed key stays in history **forever**. If it happens, say so immediately.

---

# Part 3 · Fixing mistakes (still your own repo)

> Git is a safety net. Almost nothing is permanent. **`HEAD~1`** = the commit before the current one.

```bash
git restore <file>              # throw away un-committed changes in a file
git restore --staged <file>     # take a file OUT of the box (keep the change)
git commit --amend -m "better"  # fix the last commit's message   (only if NOT pushed)
```

### The three resets — same undo, three depths
```bash
git reset --soft  HEAD~1        # undo commit → work stays IN THE BOX (staged)
git reset --mixed HEAD~1        # undo commit → work stays ON THE DESK (unstaged)  [default]
git reset --hard  HEAD~1        # undo commit → work is BINNED  ⚠️
```
```
--soft  → back to the box     --mixed → back to the desk     --hard → in the bin 💀
```

### Undo something already on the server — safely
```bash
git revert <commit-id>          # makes a NEW commit that undoes the old one (safe on shared branches)
```

### The safety net — nothing is truly lost
```bash
git reflog                      # a log of EVERYTHING for 90 days — including "deleted" commits
git reset --hard HEAD@{1}       # bring back what reflog shows
```
> **If you think you lost work, run `git reflog` FIRST.** It's almost always still there.

---

# Part 4 · The shared team repo

Now we all use **one** repo. `main` is locked — you'll see why.

```bash
cd ~
git clone https://github.com/OlimpiuStefan/techstart-team-directory.git
cd techstart-team-directory
git branch -a              # see: main AND develop
git status                 # On branch develop  (the default branch)
```

### Try to push to `main` — you can't (that's the point)
```bash
git checkout main
git pull
# make a small edit to TEAM.md, save
git commit -am "test: can I push to main?"
git push origin main       # → ! [remote rejected] (protected branch)
```
```bash
git reset --hard origin/main   # undo — put your local main back to the server's version
git checkout develop           # back to where work happens
```
*`main` is production. You reach it only through a reviewed pull request.*

---

# Part 5 · Branches & the team structure

```
  main ───────────────●     production. read-only. only the trainer merges here.
                     /
  develop ─●──●──●──●        the team's branch. all work lands here (1 approval).
           \      /
  feature   ●────●          your work. one branch per task. free.
```

**Rules:** never work directly on `main` or `develop`. Start from `develop`, make a `feature/` branch, come back via a pull request.

**Branch name (ticket-style, like the slides):** `feature/TS-<NN>-<description>` — your `<NN>` is your number from the table below.
✅ `feature/TS-07-add-profile`   ❌ `fix`, `test`, `branch2`

```bash
git checkout develop
git pull
git branch                 # * develop  ← the star is where you are
git checkout -b feature/TS-07-test   # make a branch + jump onto it
git log --oneline          # same commits! a branch is a sticky note, not a copy
git checkout develop
git branch -d feature/TS-07-test     # delete it
```

---

# Part 6 · Review rotation — find your team & number

Three exercise rounds. **Each round you review a different teammate**, so by the end you've reviewed all three. Each cell below = **who you assign your PR to** (they review you). GitHub then sends you the PR *they* assigned to you.

**Team 2 · room 1**
| Seat | Name | Your branch # | R1 assign to | R2 assign to | R2b assign to |
|---|---|---|---|---|---|
| 1 | Anna Leung | TS-01 | Benjamin | Kyle | Alexander |
| 2 | Benjamin Martins | TS-02 | Kyle | Alexander | Anna |
| 3 | Kyle Mulloy | TS-03 | Alexander | Anna | Benjamin |
| 4 | Alexander Troetsch | TS-04 | Anna | Benjamin | Kyle |

**Team 8 · room 2**
| Seat | Name | Your branch # | R1 assign to | R2 assign to | R2b assign to |
|---|---|---|---|---|---|
| 1 | Brunna Meirelles | TS-05 | Esmeralda | Joshua | Natalio |
| 2 | Esmeralda Gonzalez Menera | TS-06 | Joshua | Natalio | Brunna |
| 3 | Joshua Radjavitch | TS-07 | Natalio | Brunna | Esmeralda |
| 4 | Natalio Gomes | TS-08 | Brunna | Esmeralda | Joshua |

**Team 13 · room 3**
| Seat | Name | Your branch # | R1 assign to | R2 assign to | R2b assign to |
|---|---|---|---|---|---|
| 1 | Adriano Andrade | TS-09 | Faizan | Harish | Pragnya |
| 2 | Faizan Shamsi | TS-10 | Harish | Pragnya | Adriano |
| 3 | Harish Sundar | TS-11 | Pragnya | Adriano | Faizan |
| 4 | Pragnya Kunamneni | TS-12 | Adriano | Faizan | Harish |

**Team 14 · room 4**
| Seat | Name | Your branch # | R1 assign to | R2 assign to | R2b assign to |
|---|---|---|---|---|---|
| 1 | Chase Blancher | TS-13 | Khaled | Makayla | Noga |
| 2 | Khaled Abdelrahman | TS-14 | Makayla | Noga | Chase |
| 3 | Makayla Wray | TS-15 | Noga | Chase | Khaled |
| 4 | Noga Kojokaro | TS-16 | Chase | Khaled | Makayla |

### How to review anyone's PR
Open their PR → **Files changed** tab (that's the diff) → read it → click a line → **leave one real comment** (a question or suggestion — "LGTM" doesn't count) → **Review changes → Approve**.

**Review rules:** the author merges (not the reviewer) · comment on the code, not the person · don't approve what you didn't read.

---

# Round 1 · Your first pull request (no conflict)

Everyone adds their **own** profile file — different files, so **no conflicts**, merge in any order.

```bash
# 1. start fresh from develop
git checkout develop
git pull

# 2. your feature branch (your number)
git checkout -b feature/TS-07-add-profile

# 3. your change — copy the template, fill it in in VS Code
cp profiles/_template.md profiles/anna-leung.md      # lowercase-with-dashes filename

# 4. look before you leap
git status
git diff

# 5. stage & commit
git add profiles/anna-leung.md
git commit -m "feat: add Anna Leung profile"

# 6. push
git push -u origin feature/TS-07-add-profile
```

**On GitHub** (git prints a link — click it):
1. Check the target is **`develop`, not `main`**.
2. Title: `feat: add <Name> profile`.
3. Description: what, why, how you tested.
4. **Assign your R1 reviewer** (from the table).
5. **Create pull request.**

**Then:** review the PR of the person who assigned to you → when your PR is approved → **Squash and merge → Delete branch** → sync:
```bash
git checkout develop
git pull
git branch -d feature/TS-07-add-profile
```

---

# Round 2 · Conflict, with `git merge`

Everyone on your team adds a row to **your team's table** in `TEAM.md` — same spot → **conflicts**. Resolve one at a time, in **seat order 1→2→3→4** (develop moves after each merge).

```bash
# 1. start fresh
git checkout develop
git pull

# 2. your branch
git checkout -b feature/TS-07-team

# 3. in TEAM.md, add your row under YOUR team's heading (## Team 2 / 8 / 13 / 14):
#    | Anna Leung | Frontend Developer | [profile](profiles/anna-leung.md) |

# 4. commit & push
git add TEAM.md
git commit -m "docs: add Anna Leung to the team table"
git push -u origin feature/TS-07-team
```
Open a PR into `develop`, assign your **R2 reviewer**.

### When your PR says "This branch has conflicts" — it's your turn:
```bash
git checkout develop
git pull origin develop     # get the rows merged so far
git checkout feature/TS-07-team
git merge develop           # CONFLICT (content): Merge conflict in TEAM.md
```
Open `TEAM.md`. You'll see:
```
<<<<<<< HEAD
| your row |
=======
| your teammate's row |
>>>>>>> develop
```
**Keep BOTH rows. Delete the three marker lines** (`<<<<<<<`, `=======`, `>>>>>>>`). Save. Then:
```bash
git add TEAM.md
git commit                  # git wrote the merge message — just save & close
git push                    # a NORMAL push — no force needed
```
Reviewer approves → you **Squash and merge → Delete branch**. Next seat's turn.

> 🆘 Lost? **`git merge --abort`** puts you back exactly where you started. Nothing lost.

### Your team's order & who approves (Round 2)

**Team 2** — Anna(1) · Benjamin(2) · Kyle(3) · Alexander(4)
1. **Anna** (TS-01) goes first — her PR has no conflict (she's the first to touch the table). **Kyle** approves it, Anna merges. → The shared team table on `develop` now has: **Anna**.
2. **Benjamin** (TS-02) — his turn now. He runs `git merge develop`, which pulls in Anna's row → git shows a conflict (Anna's row vs his). He keeps **both** rows, deletes the markers, pushes. **Alexander** approves, Benjamin merges. → `develop` now has: **Anna, Benjamin**.
3. **Kyle** (TS-03) — `git merge develop` now pulls in Anna + Benjamin → conflict → he keeps **all three** rows, pushes. **Anna** approves, Kyle merges. → `develop` now has: **Anna, Benjamin, Kyle**.
4. **Alexander** (TS-04) — `git merge develop` pulls in the three → he keeps **all four** rows, pushes. **Benjamin** approves, Alexander merges. → `develop` now has: **all four rows** ✅ Team 2's table is complete.

**Team 8** — Brunna(1) · Esmeralda(2) · Joshua(3) · Natalio(4)
1. **Brunna** (TS-05) — clean, first. **Joshua** approves → merge.
2. **Esmeralda** (TS-06) — merge develop → keep both → push. **Natalio** approves → merge.
3. **Joshua** (TS-07) — merge develop → keep all 3 → push. **Brunna** approves → merge.
4. **Natalio** (TS-08) — merge develop → keep all 4 → push. **Esmeralda** approves → merge. develop: all 4 ✅

**Team 13** — Adriano(1) · Faizan(2) · Harish(3) · Pragnya(4)
1. **Adriano** (TS-09) — clean, first. **Harish** approves → merge.
2. **Faizan** (TS-10) — merge develop → keep both → push. **Pragnya** approves → merge.
3. **Harish** (TS-11) — merge develop → keep all 3 → push. **Adriano** approves → merge.
4. **Pragnya** (TS-12) — merge develop → keep all 4 → push. **Faizan** approves → merge. develop: all 4 ✅

**Team 14** — Chase(1) · Khaled(2) · Makayla(3) · Noga(4)
1. **Chase** (TS-13) — clean, first. **Makayla** approves → merge.
2. **Khaled** (TS-14) — merge develop → keep both → push. **Noga** approves → merge.
3. **Makayla** (TS-15) — merge develop → keep all 3 → push. **Chase** approves → merge.
4. **Noga** (TS-16) — merge develop → keep all 4 → push. **Khaled** approves → merge. develop: all 4 ✅

---

# Round 2b · Same conflict, with `git rebase` (if we run it)

Same as Round 2, but you **rebase** instead of merge. Add yourself under your team's **standup** heading in `TEAM.md`.

```bash
git checkout develop && git pull
git checkout -b feature/TS-07-standup
# add "- Anna Leung" under your team's standup heading (### Team 2 / 8 / 13 / 14)
git add TEAM.md
git commit -m "docs: add TS-07 to standup order"
git log --oneline -1        # ⭐ write down your commit ID — you'll compare it after
git push -u origin feature/TS-07-standup
```
Open a PR into `develop`, assign your **R2b reviewer**. When it's your turn (conflict appears):

```bash
git fetch origin
git rebase origin/develop   # CONFLICT in TEAM.md
```
> ⚠️ **The markers are FLIPPED in a rebase:** `HEAD` is now `develop`, and the part **below** `=======` is **your** line. Don't trust the labels — read the content, keep all rows, delete the markers.
```bash
git add TEAM.md
git rebase --continue       # editor may open — save & close
git push --force-with-lease # ⚠️ rebase rewrote your commit → needs force. NEVER plain --force.
git log --oneline -1        # same message, DIFFERENT ID — it's a copy
```
Reviewer approves → **Squash and merge → Delete branch**.

> 🆘 Lost? **`git rebase --abort`** puts you back exactly where you started.

### Your team's order & who approves (Round 2b)
Same seat order 1→2→3→4, but a **different reviewer** (R2b column, seat N+3).

**Team 2** — Anna(1) · Benjamin(2) · Kyle(3) · Alexander(4)
1. **Anna** (TS-01) — clean, first. **Alexander** approves → merge.
2. **Benjamin** (TS-02) — rebase → keep both → force-with-lease. **Anna** approves → merge.
3. **Kyle** (TS-03) — rebase → keep all 3 → force-with-lease. **Benjamin** approves → merge.
4. **Alexander** (TS-04) — rebase → keep all 4 → force-with-lease. **Kyle** approves → merge. develop: all 4 ✅

**Team 8** — Brunna(1) · Esmeralda(2) · Joshua(3) · Natalio(4)
1. **Brunna** (TS-05) — clean, first. **Natalio** approves → merge.
2. **Esmeralda** (TS-06) — rebase → keep both → force-with-lease. **Brunna** approves → merge.
3. **Joshua** (TS-07) — rebase → keep all 3 → force-with-lease. **Esmeralda** approves → merge.
4. **Natalio** (TS-08) — rebase → keep all 4 → force-with-lease. **Joshua** approves → merge. develop: all 4 ✅

**Team 13** — Adriano(1) · Faizan(2) · Harish(3) · Pragnya(4)
1. **Adriano** (TS-09) — clean, first. **Pragnya** approves → merge.
2. **Faizan** (TS-10) — rebase → keep both → force-with-lease. **Adriano** approves → merge.
3. **Harish** (TS-11) — rebase → keep all 3 → force-with-lease. **Faizan** approves → merge.
4. **Pragnya** (TS-12) — rebase → keep all 4 → force-with-lease. **Harish** approves → merge. develop: all 4 ✅

**Team 14** — Chase(1) · Khaled(2) · Makayla(3) · Noga(4)
1. **Chase** (TS-13) — clean, first. **Noga** approves → merge.
2. **Khaled** (TS-14) — rebase → keep both → force-with-lease. **Chase** approves → merge.
3. **Makayla** (TS-15) — rebase → keep all 3 → force-with-lease. **Khaled** approves → merge.
4. **Noga** (TS-16) — rebase → keep all 4 → force-with-lease. **Makayla** approves → merge. develop: all 4 ✅

**Merge vs rebase:** merge adds one commit joining the two lines (honest, safe, normal push). Rebase re-writes your commits on top (straight line, but new IDs → force-push). We default to **merge**.

---

# Round 3 · Try to break `main` (you can't)

```bash
git checkout main
git pull
echo "urgent fix" >> TEAM.md
git commit -am "fix: straight into main"
git push origin main        # → ! [remote rejected] (protected branch)
git reset --hard origin/main    # clean up
```
Also try opening a PR from a branch **into `main`**: the merge button stays grey — only the trainer (code owner) can approve it. *`main` is production. No one touches it directly.*

---

# Round 4 · The release

**The trainer does this one — you watch.** The trainer opens a pull request **`develop → main`** (title `release: merge develop into main`), and merges it with **Merge commit** — because only the trainer can merge into `main`. This is the release: everything the whole team built today, going into `main` in one go.

Then everyone syncs their own machine:
```bash
git checkout main
git pull                    # bring the release down to your laptop
git lg                      # see the whole team's work, now on main
```

> **On a real team:** the person who opens and merges this release PR is called the **release manager** — usually a senior dev or a rotating role, not everyone. They gather the team's approvals, make sure everything's ready, and push the button. Today that's the trainer; on your projects it'll be a named person for each release.

---

# 🆘 Quick reference

```bash
git status                     # where am I?  ← run this all the time
git diff / git diff --staged   # changes on the desk / in the box
git add <file> / git restore --staged <file>   # into / out of the box
git commit -m "type: message"  # seal the box   (feat / fix / docs / chore)
git push / git pull            # send to / get from GitHub
git log --oneline / git lg     # history
git checkout -b <branch>       # make + switch branch
git branch -d <branch>         # delete branch

# fix mistakes
git restore <file>             # drop un-committed changes
git reset --soft/--hard HEAD~1 # undo last commit (keep work / bin work)
git revert <id>                # undo safely on shared branches
git reflog                     # 🔴 find "lost" work

# conflicts (one at a time, seat order)
git merge develop  →  fix markers  →  git add . && git commit && git push
git merge --abort              # 🆘 start over
```

**Six things to remember:** ① `git status` after everything ② one branch per task ③ small commits, messages that say why ④ never touch `main` ⑤ nothing is lost — `git reflog` ⑥ a conflict is not an error, it's a question.
