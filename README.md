# Git Recovery Practice

This repo is a **safe sandbox** to practice undoing mistakes in a shared GitHub repo using **GitHub Desktop** or **Git (command line)**.

## Setup for Github Desktop

Clone your **team's** practice repo from Github:

File -> Clone Repository

---

## 🧑‍💻 Using VS Code (Git Commands Version)

If you prefer using **VS Code + Git (CLI)** instead of GitHub Desktop, here are the equivalent commands for each workflow.

> You can run these in:
> - VS Code Terminal (`Ctrl + ~`)
> - Git Bash
> - Mac/Linux Terminal

---

## Setup for VS Code

Clone your **team's** practice repo from Github:

git clone <your-team-repo-url>
cd git-recovery-practice-team-X

## 🔁 Core Workflow (CLI version)

```bash
git pull origin main
git checkout -b yourname/task
git add .
git commit -m "Your message here"
git push origin yourname/task
```

---

## 🧪 Part 1 — Discard Uncommitted Changes

```bash
git restore files/story.md
```

---

## 🧪 Part 2 — Undo a Local Commit (NOT pushed)

```bash
git reset --soft HEAD~1
```

To completely discard changes:

```bash
git reset --hard HEAD~1
```

⚠️ This permanently deletes changes.

---

## 🧪 Part 3 — Revert a Merged (Pushed) Commit

```bash
git revert HEAD
```

---

## 🧪 Part 4 — Handling Merge Conflicts

```bash
git pull origin main
```

Resolve conflict markers in file, then:

```bash
git add files/story.md
git commit
```

---

## 🧪 Part 5 — Switch to Backup Branch

```bash
git checkout backup-before-fixing
git checkout yourname/task
```

---

## 🧠 Key Concepts (CLI mindset)

| Situation                | Command       | Safe for Teams?      |
| ------------------------ | ------------- | -------------------- |
| Undo uncommitted changes | `git restore` | ✅ Yes                |
| Undo local commit        | `git reset`   | ⚠️ Only if not pushed |
| Undo shared commit       | `git revert`  | ✅ Yes                |

## Core rule for this lab
**Always work on a branch.**  
Do not commit directly to `main`.

**Workflow (every time):**
1. Fetch + Pull
2. Create a branch: `yourname/task`
3. Make changes
4. Commit on your branch
5. Push your branch
6. Open a Pull Request (PR) into `main`
7. Review + merge
8. Pull `main` again

---

## What you’ll practice
1. Discard uncommitted changes
2. Undo a local commit (not pushed)
3. Revert a merged (pushed) mistake (team-safe)
4. Resolve a merge conflict
5. Use a backup branch to recover

---

## Files to know
- `files/story.md` – conflict-friendly text file (you will edit the same lines as teammates)
- `files/numbers.csv` – small CSV for “bad change → revert” practice

---

## Lab steps (GitHub Desktop)

### Part 0 — Safety branch (do this first)
1. **Branch → New Branch…**
2. Name: `backup-before-fixing`
3. Create

> If you get stuck later, you can always switch back to this branch.

---

### Part 1 — Discard uncommitted changes (solo)
1. Create a branch: `yourname/discard-demo`
2. Open `files/story.md` and add a messy line at the top:
   `I AM TYPING RANDOM STUFF HERE!!!`
3. Save the file and confirm it appears under **Changes**
4. Right-click `files/story.md` → **Discard Changes**
5. Confirm the messy line is gone
6. (Optional) Delete your branch or just leave it

---

### Part 2 — Undo a commit that hasn’t been pushed (solo)
1. Create a branch: `yourname/undo-demo`
2. Add a line to the bottom of `files/story.md`:
   `Draft change: add a new sentence.`
3. Commit message: `WIP: draft change`
4. **DO NOT PUSH**
5. Go to **History** and click **Undo**
6. Confirm your change is back under **Changes**
7. Discard it, or improve it and recommit

---

### Part 3 — Revert a merged mistake (team-safe)
This simulates a mistake that is already shared.

1. Create a branch: `yourname/bad-csv`
2. Edit `files/numbers.csv` (change a few values)
3. Commit message: `Bad edit to numbers`
4. Push your branch
5. Open a PR and **merge it into `main`** (yes, on purpose)
6. Pull `main`
7. Create a new branch: `yourname/revert-csv`
8. Revert the bad commit:
   - Use GitHub web UI (**Commits → select commit → Revert**) OR
   - If Desktop shows Revert, use it
9. Push the revert branch
10. Open PR → merge into `main`
11. Pull `main`

---

### Part 4 — Merge conflict drill (pairs)
You will intentionally create a conflict on **the same line** in `files/story.md`.

**Work in Pairs**

#### Student A
1. Branch: `A/conflict`
2. Edit line marked `LINE_TO_CONFLICT` so it reads:
   `LINE_TO_CONFLICT: Student A was here.`
3. Commit: `Edit conflict line (A)`
4. Push branch → open PR → **merge to main**
5. Tell Student B you merged

#### Student B
1. Pull `main` **before starting**, then:
2. Branch: `B/conflict`
3. Edit the same line so it reads:
   `LINE_TO_CONFLICT: Student B was here.`
4. Commit: `Edit conflict line (B)`
5. Push branch → open PR
6. When GitHub shows a conflict, choose **Resolve conflicts**
7. Make the final line:
   `LINE_TO_CONFLICT: Student A and Student B were here.`
8. Mark resolved, complete merge, pull `main`

✅ Skill: **Conflict markers + resolution mindset**

---

### Part 5 — Recovery using a backup branch
If anything feels broken:
1. Switch to `backup-before-fixing`
2. Verify files look sane
3. Switch back to your working branch or pull `main`
4. Continue
