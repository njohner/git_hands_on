# Git: a hands-on course

This repository is meant to provide both slides and exercises to better understand and learn to use git.

## Presentation

The presentation is written in Markdown format and can be converted to a usable format (html, pdf, etc.) using [quarto](https://quarto.org).

For that you will need to:
- install `quarto`
- make sure you have [R](https://www.r-project.org/) with all the necessary dependencies. This can be achieved with conda `conda env create -f conda/presentation_env.yaml`
- Install quarto extensions in `presentation` folder:
    - `quarto install extension andrie/reveal-auto-agenda`
    - `quarto install extension grantmcdermott/quarto-revealjs-clean`
    - `quarto add reuning/codefocus`

Viewing the slides can then be simply achieved with
```
conda activate quarto_r
quarto preview presentation/presentation.qmd
```
which will open a browser window displaying the slides.

To get the `html` file of the presentation you can instead run
```
conda activate quarto_r
quarto preview presentation/presentation.qmd --render revealjs
```
and if you want to have a self contained version of the presentation, you will need the copy the following files and folders:

```
presentation/presentation.html
presentation/presentation_files
presentation/figures
```

## Exercises

As we work through the exercises we will try to keep the repository clean, so that each exercise can be done independently. We will therefore work on separate branches.

### Ex. 1: Recording changes
- Create a branch from master and switch to it: `git switch -c ex1 master`
- Modify `training/file1.md`, stage the changes and commit them.
- Now modify `training/file2.md`, add some text lines before the current content and some after the current content.
- Only stage the first block of changes.
- Show the staged changes.
- Show the changes that were not staged.
- Commit.
- Stage the remaining changes to `training/file2.md` and commit them.
- Display the history for the last 3 commits.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch -c ex1 master
# modify training/file1.md
git add training/file1.md
git commit -m 'Modified file1.'
# modify training/file2.md
git add -i training/file2.md
git diff --staged
git diff
git commit -m 'Modify file2.'
git add training/file2.md
git commit -m 'More modifications to file2.'
git log -n3
```
</details>


### Ex. 2: working with branches
#### Ex. 2.1: Creating and using branches
- Check on which branch you currently are
- If not on `master`, switch to `master`
- Create a new branch `ex2` and switch to it
- Modify `training/file1.md` and `training/file2.md`
- Stage the changes in `training/file1.md` and commit them.
- Switch to `master`:
    - Notice that you still have the changes to `training/file2.md` in your working directory
    - Notice that the changes to `training/file1.md` that you have just made are gone. Of course they are not lost, they are in the commit on branch `ex2`. You can display that difference with `git diff ex2 training/file1.md`
- Create a new branch `ex2b` and switch to it
- Stage `training/file2.md` and commit

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git branch
# if not on master: git switch master
git switch -c ex2
# modify training/file1.md and training/file2.md
git add training/file1.md
git commit -m "Modified file1."
git switch master
git diff ex2 training/file1.md
git switch -c ex2b
git add training/file2.md
git commit -m "Modified file2."
```
</details>

#### Ex. 2.2: Rebasing
- Look at the current history with `git log -n6 --oneline --graph --decorate --all`
- We will now rebase branch `ex2b` onto branch `ex2`:
    - If you are not on branch `ex2b`, switch to it
    - rebase on branch `ex2`
    - Look at the current history again, as above

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git log -n6 --oneline --graph --decorate --all
# if not on ex2b: git switch ex2b
git rebase ex2
git log -n6 --oneline --graph --decorate --all
```
</details>

#### Ex. 2.3: Fast-forward merge
- switch over to `ex2`
- merge `ex2b` into `ex2`
- Look at the current history with `git log -n6 --oneline --graph --decorate --all`
- Now delete the `ex2b` branch

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch ex2
git merge ex2b
git log -n6 --oneline --graph --decorate --all
git branch -d ex2b
```
</details>

#### Ex. 2.4: Conflict resolution
Let's go ahead and create a conflict
- Switch to `master` branch
- Create new branch `ex2c` and switch to it
- Modify `training/file2.md` and commit theses changes
- Take a look at the history (`git log -n6 --oneline --graph --decorate --all`)
- Rebase that branch onto `ex2`. This should lead to a conflict
- `git status` should tell you that two commits have modified `training/file2.md` and what to do:
    - Reconcile the 2 sets of changes to that file
    - Stage that file
    - continue the rebase process
- Take another look at the history.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch master
git switch -c ex2c
# modify training/file2.md
git add training/file2.md
git commit -m "More modifications in file2"
git log -n6 --oneline --graph --decorate --all
git rebase ex2
# modify training/file2.md to resolve the conlict
git add training/file2.md
git rebase --continue
git log -n6 --oneline --graph --decorate --all
```
</details>

#### Ex. 2.4: Deleting branches
We'll now do some clean-up:
- Switch to `master` branch
- Delete all other branches. For some branches, git will complain that the branch was not fully merged, and you'll have to force delete them, git will tell you how (use `git branch -D <branchname>`)

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch master
git branch -D ex2
git branch -D ex2c
```
</details>

### Ex. 3: The stash
We assume you are working on `training/file1.md` on two different branches, a `dev` branch and a `hotfix` branch. Let's set that up:
- Switch to a new branch `hotfix` (from master)
- Modify `training/file1.md` and commit these changes
- Switch to master
- Create a new branch `dev` and switch to it
- Modify `training/file1.md`, but do not commit

You're interrupted in your work and quickly need to do something on the `hotfix` branch:
- Try to switch to `hotfix` branch. This should fail with a warning that your local changes to `training/file1.md` would be overwritten.
- Stash your changes
- Switch to `hotfix`
- Fix your last commit:
    - Modify `training/file1.md` some more.
    - Stage and commit these changes.
- Go back to what you were doing:
    - Switch to `dev` branch
    - Retrieve your changes from the stash.
    - Stage and commit `training/file1.md`
- Clean-up: switch to master and delete other branches

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch -c hotfix
# modify training/file1.md
git add training/file1.md
git commit -m "Hotfix in file1."
git switch master
git switch -c dev
# modify training/file1.md
git switch hotfix
git stash
git switch hotfix
# modify training/file1.md
git add training/file1.md
git commit -m "Fix the hotfix!."
git switch dev
git stash pop
git add training/file1.md
git commit -m "Modified file1."
git switch master
git branch -D hotfix
git branch -D dev
```
</details>

### Ex. 4: Rewriting history

#### Ex. 4.1: Amending the last commit
We will start simple, by modifying the last commit.
- Switch to a new branch `ex4` (from master)
- Modify `training/file1.md` and commit the changes

Now you realize that you want to modify the last commit, for example you want to fix a typo in the commit and do not want a separate commit for that.
- Modify `training/file1.md` some more, then amend the changes to the last commit.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git switch -c ex4
# modify training/file1.md
git add training/file1.md
git commit -m "Modified file1."
# modify training/file1.md some more
git add training/file1.md
git commit --amend
```
</details>

#### Ex. 4.2: Interactive rebasing
Make two more commits (still on branch ex4):
- Modify `training/file2.md` and commit the changes
- Modify `training/file1.md` and commit the changes

Now as above you realize it would be cleaner if you had a single commit modifying `training/file1.md`. You can rewrite the history using an interactive rebase.
- Interactively rebase the last 3 commits.
- In the interactive mode, change the order of commits. Move the second to last commit (the one modifying `training/file2.md` to last position and squash the two commits modifying `training/file1.md` together)
- Look at the history

<details>
<summary>${\color{red}Answer}$</summary>

```bash
# modify training/file2.md
git add training/file2.md
git commit -m "Modify file2."
# modify training/file1.md
git add training/file1.md
git commit -m "Modify file1 some more."
git rebase -i HEAD~3
git log -n3
```
</details>

### Ex. 5: Undoing things
We go on working on branch `ex4`. If you don't have that branch, simply create a new branch and add 2 commits.

#### Ex. 5.1: Undoing the last commit
Ok that last commit is really bad and you want to undo it.
- Do a soft reset to undo the last commit (to select the last commit you can use `HEAD~1` or use the hash of the commit you want to reset to).
- do a `git status`. You'll see that the changes are still there, but not committed anymore, instead they are staged

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git reset --soft HEAD~1
git status
```
</details>

#### Ex. 5.2: Unstaging
Unstage the changes to `training/file1.md`. If you don't know how, look at the output of `git status`.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git restore --staged training/file2.md
```
</details>

#### Ex. 5.3: Drop changes from work directory
You really don't want these changes, drop them from the working directory. Again if you don't know how, do a `git status`.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git restore training/file2.md
```
</details>

#### Ex. 5.4: Undoing the last commit and dropping the changes
We could have done the same thing in one go, using a hard reset. We'll try that now. Undo the last commit and drop the corresponding changes using a hard reset.

<details>
<summary>${\color{red}Answer}$</summary>

```bash
git reset --hard HEAD~1
```
</details>

## Resources

- [Pro Git](https://git-scm.com/book): great reference book for everything git. Many of the figures from the presentation come from its [git repository](https://github.com/progit/progit2).
