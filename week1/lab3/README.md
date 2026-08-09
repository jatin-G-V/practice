# Lab 3 – Git Branching and Pull Request Workflow

## Objective

The objective of this lab is to practice a collaborative Git workflow by creating a feature branch, making incremental commits, opening a Pull Request (PR), incorporating review feedback, and merging changes into the main branch.

---

## Tasks Performed

### 1. Created a Feature Branch

Created a new feature branch from the `main` branch.

```bash
git checkout -b feature/word-count
```

---
<img width="1003" height="118" alt="Screenshot From 2026-08-07 15-54-23" src="https://github.com/user-attachments/assets/6337c6dc-c47d-4afb-ac8a-1cf06dcd7df1" />


### 2. Implemented Incremental Changes

Made multiple small and meaningful commits instead of one large commit.



---
<img width="1412" height="340" alt="Screenshot From 2026-08-07 15-57-05" src="https://github.com/user-attachments/assets/804af034-d568-47d2-b40c-c06e55bd234e" />

### 3. Pushed Feature Branch

Pushed the feature branch to the remote repository.

```bash
git push -u origin feature/word-count
```

---

### 4. Opened a Pull Request

Created a Pull Request from:

```
feature/word-count → main
```

Included a summary of changes and the purpose of the update.

---
<img width="1421" height="431" alt="Screenshot From 2026-08-07 16-01-57" src="https://github.com/user-attachments/assets/0e7ea166-4594-498a-8851-d022623d1cb1" />

### 5. Code Review

Received the following review suggestion:

> Use `str.translate()` instead of repeatedly calling `replace()` in the `word_count()` function.

Updated the implementation based on the review and pushed the changes.

---
<img width="1436" height="498" alt="Screenshot From 2026-08-07 16-42-16" src="https://github.com/user-attachments/assets/85c62d68-c477-46c9-bd1b-4de014d6cff9" />

### 6. Merged the Pull Request

After completing the review process, the Pull Request was merged into the `main` branch.

---
<img width="1048" height="543" alt="Screenshot From 2026-08-07 16-43-16" src="https://github.com/user-attachments/assets/dfd003bb-0aef-4eaa-b9cb-38097ba940c8" />

### 7. Deleted the Feature Branch

Deleted the feature branch after the merge.

Local:

```bash
git branch -d feature/word-count
```

Remote:

```bash
git push origin --delete feature/word-count
```

---
<img width="996" height="358" alt="Screenshot From 2026-08-07 16-44-57" src="https://github.com/user-attachments/assets/2bda39b2-a712-4d30-8241-eca99d2f8945" />

## Git Commands Used

```bash
git checkout -b feature/word-count
git add .
git commit -m "used str.translate() for punctuation removal"
git push -u origin feature/word-count
git checkout main
git pull
git branch -d feature/word-count
git push origin --delete feature/word-count
```

---

## Concepts Covered

- Git Branching
- Feature Branch Workflow
- Incremental Commits
- Conventional Commit Messages
- Pull Requests
- Code Review
- Code Refactoring
- Branch Merging
- Branch Deletion

---

## Project Structure

```text
lab3/
└── README.md
```

---

## Learning Outcomes

After completing this lab, I learned how to:

- Work on a separate feature branch.
- Create multiple meaningful commits.
- Push feature branches to GitHub.
- Create and manage Pull Requests.
- Incorporate review feedback into the code.
- Merge changes into the main branch.
- Delete feature branches after merging.
- Follow a collaborative Git workflow similar to real-world software development.
