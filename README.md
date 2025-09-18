# Course on collaboratory software development

This is a quick course on some fundamentals in working together on a coding project

Accompanying presentation can be found here [Google Docs](https://docs.google.com/presentation/d/1eP0Suryhu-Fw2E44i8wFQtQ7nGVxYQG9aNoj4_GEGYA/edit?usp=sharing)

## Task 0: Initial Setup

For this workshop, you will need to have Git, UV and Python installed on your machine and have a GitHub account.

- Create a github account [Github](https://github.com/) if you don't have one already
- Also save this for later [GitHub Student Developer Pack](https://education.github.com/pack) for some free goodies for the rest of your time studying.

If you don't have git installed, follow the instructions below to install it.

- Install git on your machine
  - [Windows](https://git-scm.com/download/win)

    - Press `Win + R` then write `cmd`

    ```cmd
      winget install --id Git.Git -e --source winget
    ```

    Or download installer from [The official Github page](https://github.com/git-for-windows/git/releases/download/v2.51.0.windows.1/Git-2.51.0-64-bit.exe)

  - [Mac](https://git-scm.com/download/mac)

    - Make sure to have brew installed if you don't have it follow [this](https://brew.sh/)

    ```bash
    brew install git
    ```

  - [Linux](https://git-scm.com/download/linux)

    - You probalby allready have Git preinstalled lmao enjoy
    - If you somehow don't gave git see [here](https://git-scm.com/download/linux) for instructions for your distro

To validate that git is installed, open a terminal/cmd and write

```bash
git --version
```

- Initial configuration of git:

  - Set your name and the email you used On Github

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

  - Additionally you can set a default merge policy globally (this is normally asked on a per repo basis). We recommend the following option:

  ```bash
  git config --global pull.rebase false
  ```

If you get a version number, you are good to go.

- Install UV package manager follow the directions at the [official docs](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

- Lastly if you don't have Python installed you can easily do so with the following command:

```bash
uv python install
```

## Task 1: Fork and clone the repo

Forking the repository will save a copy to your own Github page, where you can do as you please with it. Since we will be making some changes as part of the tasks this is required.

- Go to the [fork page](https://github.com/CogitoNTNU/course-on-collaboratory-software-development/fork) for the repo or click on the fork button in the top right on the \<>Code tab of the project.

- Clone the repository in the directory of your choosing (open a terminal/cmd in that directory) and clone **your** recently forked repository. Change fill in your own username in the url bellow

```bash
git clone https://github.com/[YOUR GITHUB USERNAME]/course-on-collaboratory-software-development.git
cd course-on-collaboratory-software-development
```

## Task 2: Making a change

This course is accompanied by a simple calculator program. The program is not complete and your task is to implement the missing functionality. You will find the code in `src/calculator.py`

1. In a terminal/cmd in the project's root directory install and activate the development environment

```bash
uv sync
```

2. Set up the pre-commit

```bash
uv run pre-commit install
```

3. Open the project in your favorite editor and implement the missing functionality in `src/calculator.py`. The missing functionality is marked with a `# TODO` comment (3 in total).

To try out your changes, run the program with

```bash
uv run python main.py
```

4. When you are done, stage, commit and push your changes

```bash
git add src/calculator.py
git commit -m "Your commit message"
git push
```

## Task 3: Collaborating with others

Now that you have implemented division, your simulated team mates has done their work in a separate branch `add-multiplication`. You are now tasked with integrating their changes with your's.

- Use the following commands to list and switch to their branch to check out the work:

```bash
git fetch --all 
git switch add-multiplication
```

You will now have to either review the pull request in Github or just merge the changes to main locally before pushing. You might find that you have a conflict you need to resolve...

```bash
git switch main
git merge add-multiplication
```

When resolving a conflict you decide what to keep, what to discard and how the files end up. Once you are happy with the outcome finish the merge by staging, commiting and pushing your changes.

```bash
git add .
git commit -m "Your commit message"
git push
```

## Task 4: Add a new dependency

Your team needs a new dependency, let's say `numpy` for some reason. You need to add this dependency to the project.

- Add the dependency with uv

```bash
uv add numpy
```

- Check out the changes to the `pyproject.toml` and `uv.lock` files.
- Stage, commit and push the changes

## Task 5: Task 5: Change workflow

This task involves GitHub actions.

- You will find the workflow file in `.github/workflows/ci.yml`. The workflow is a simple CI pipeline that shall runs tests and lints the code.
- Change the last step in the `build-and-test` job to actually run the tests with `uv run pytest` instead of just echoing a TODO message.
