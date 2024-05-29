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
- Use `git add -i training/file2.md` to only stage the first block of changes.
- Show the staged changes.
- Show the changes that were not staged.
- Commit
- Stage the remaining changes to `training/file2.md` and commit them.
- Display the history for the last 3 commits.


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

#### Ex. 2.2: Rebasing
- Look at the current history with `git log -n6 --oneline --graph --decorate --all`
- We will now rebase branch `ex2b` onto branch `ex2`:
    - If you are not on branch `ex2b`, switch to it
    - rebase on branch `ex2`
    - Look at the current history again, as above

#### Ex. 2.3: Fast-forward merge
- switch over to `ex2`
- merge `ex2b` into `ex2`
- Look at the current history with `git log -n6 --oneline --graph --decorate --all`
- Now delete the `ex2b` branch

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

#### Ex. 2.4: Deleting branches
We'll now do some clean-up:
- Switch to `master` branch
- Delete all other branches. For some branches, git will complain that the branch was not fully merged, and you'll have to force delete them, git will tell you how (use `git branch -D <branchname>`)

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


### Ex. 4: Rewriting history

#### Ex. 4.1: Amending the last commit
We will start simple, by modifying the last commit.
- Switch to a new branch `ex4` (from master)
- Modify `training/file1.md` and commit the changes

Now you realize that you want to modify the last commit, for example you want to fix a typo in the commit and do not want a separate commit for that.
- Modify `training/file1.md` some more, then amend the changes to the last commit.

#### Ex. 4.2: Interactive rebasing
Make two more commits:
- Modify `training/file2.md` and commit the changes
- Modify `training/file1.md` and commit the changes

Now as above you realize it would be cleaner if you had a single commit modifying `training/file1.md`. You can rewrite the history using an interactive rebase.
- Interactively rebase the last 3 commits: `git rebase -i HEAD~3`
- In the interactive mode, change the order of commits. Move the second to last commit (the one modifying `training/file2.md` to last position and squash the two commits modifying `training/file1.md` together)

### Ex. 5: Undoing things
We go on working on branch `ex4`. If you don't have that branch, simply create a new branch and add 2 commits.

#### Ex. 5.1: Undoing the last commit
Ok that last commit is really bad and you want to undo it.
- Do a soft reset to undo the last commit (to select the last commit you can use `HEAD~1` or use the hash of the commit you want to reset to).
- do a `git status`. You'll see that the changes are still there, but not committed anymore, instead they are staged

#### Ex. 5.2: Unstaging
Unstage the changes to `training/file1.md`. If you don't know how, look at the output of `git status`.

#### Ex. 5.3: Drop changes from work directory
You really don't want these changes, drop them from the working directory. Again if you don't know how, do a `git status`.

#### Ex. 5.4: Undoing the last commit and dropping the changes
We could have done the same thing in one go, using a hard reset. We'll try that now. Undo the last commit and drop the corresponding changes using a hard reset.

## Resources

- [Pro Git](https://git-scm.com/book): great reference book for everything git. Many of the figures from the presentation come from its [git repository](https://github.com/progit/progit2).
