# Git Cheat Sheet

**ℹ️ [git-conventional-commits](https://github.com/qoomon/git-conventional-commits)** A CLI util to ensure this conventions and generate changelogs

## Commit Message Formats

### Default

<pre>
<b><a href="#types">&lt;type&gt;</a></b></font>: <b><a href="#description">&lt;description&gt;</a></b>
</pre>

### Types

- Relevant changes
  - `feat` Commits, that adds or remove a new feature
  - `fix` Commits, that fixes a bug
- `refactor` Commits, that rewrite/restructure your code, however does not change any API behavior
- `style` Commits, that do not affect the meaning (white-space, formatting, missing semi-colons, etc)
- `test` Commits, that add missing tests or correcting existing tests
- `docs` Commits, that affect documentation only
- `build` Commits, that affect build components like build tool, ci pipeline, dependencies, project version, ...
- `chore` Miscellaneous commits e.g. modifying `.gitignore`

### Examples

- ```text
  feat: add email notifications on new direct messages
  ```
- ```text
  fix: add missing parameter to service call

  The error occurred because of <reasons>.
  ```
- ```text
  build: update dependencies
  ```
- ```text
  refactor: implement fibonacci number calculation as recursion
  ```
- ```text
  style: remove empty line
  ```

## Useful Commands

- `git status` Show the working tree status
- `git add <file>` Add file contents to the index
- `git commit -m "<message>"` Record changes to the repository with a message
- `git commit --amend -m "<message>"` Amend the last commit with a new message additionally you can use `--no-edit` to keep the old message but add new changes
- `git pull` Fetch from and integrate with another repository or a local branch
- `git fetch --all` Fetch all remotes
- `git push` Update remote refs along with associated objects
- `git log` Show commit logs
- `git log --oneline` Show commit logs in a single line
- `git diff <source_branch> <target_branch>` Show changes between branches
- `git switch <branch>` Switch branches
- `git switch -c <new_branch>` Create and switch to a new branch
- `git merge <branch>` Merge a branch into the current branch
- `git rebase <branch>` Reapply commits on top of another base tip
- `git revert <commit>` Revert a specific commit by creating a new commit
- `git stash` Stash the changes in a dirty working directory away
- `git stash pop` Apply the latest stashed changes and remove it from the stash list
- `git reset --soft HEAD~1` Undo the last commit but keep the changes staged
- `git reset origin/<branch> --hard` The nuclear option - reset your local branch to exactly match the remote branch - all local changes will be lost!
