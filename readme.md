# GitHub Repo File Counter (with GitHub Actions)

This project includes a simple **Python script** and a **GitHub Actions workflow** that counts the number of files in your repository every time you push code to the `main` branch.

It's a great example of how to automate tasks using GitHub Actions!

---

## What This Project Does

- There's a script called `count_files.py` that checks how many files exist in your repo.
- A GitHub Actions workflow runs this script automatically **every time you push code** to the `main` branch.
- The result is printed in the GitHub Actions logs.

---

## The Python Script (`count_files.py`)

This script goes through all the folders and files in your project and prints the total number of files.

```python
import os

def count_files():
    file_count = sum(len(files) for _, _, files in os.walk('.'))
    print(f"Total files in repo: {file_count}")

if __name__ == "__main__":
    count_files()
```
Save this file in a `scripts/` folder like this:
```
scripts/count_files.py
```

## The GitHub Actions Workflow (`count-files.yml`)

This workflow lives in `.github/workflows/count-files.yml` and is triggered on every `push` to the `main` branch.

Here’s what it does:

1. Checks out the code from your repo.
2. Sets up `Python 3.10` on the GitHub runner.
3. Runs the script that counts the files.

```yaml
name: repo file count

on:
  push:
    branches:
      - main

jobs:
  count-files:
    runs-on: ubuntu-latest

    steps:
      - name: checkout code
        uses: actions/checkout@v4

      - name: setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: run the count_files.py script
        run: python scripts/count_files.py

```

## How to Use This
1. Add the Python script to `scripts/count_files.py`
2. Add the workflow file to `.github/workflows/count-files.yml`
3. Push your changes to the `main` branch

GitHub will automatically run the workflow and count your files!

## It works!
On the Actions tab, the workflow automatically runs and performs the specified executes jobs

![Screenshot 2025-07-06 233507](https://github.com/user-attachments/assets/8148de19-b2a3-43ee-ad15-1ba4bb00272b)

![Screenshot 2025-07-06 233554](https://github.com/user-attachments/assets/43600fea-b320-4a28-b4a4-b6fc5b590a93)

![Screenshot 2025-07-06 233614](https://github.com/user-attachments/assets/88897fb3-01c9-43ba-a591-a2e9f517a197)

