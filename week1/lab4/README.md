# Lab 4 – Command Line and Bash

## Objective

The objective of this lab is to get comfortable with the Linux command line, text-processing utilities, pipelines, and Bash scripting by creating a reusable script to find the most frequent words in a text file.

---

## Tasks Performed

### 1. Downloaded Plain-Text Files

Downloaded two public-domain text files from Project Gutenberg using `curl -O`.

Files used:

- `pg1661.txt` – The Adventures of Sherlock Holmes
- `dracula.txt` – Dracula

Example command:

```bash
curl -O https://www.gutenberg.org/cache/epub/1661/pg1661.txt
```

```bash
curl -O https://www.gutenberg.org/cache/epub/45839/dracula.txt
```

---

### 2. Found the Most Frequent Words

Used a shell pipeline consisting of:

- `tr`
- `sort`
- `uniq -c`
- `sort -nr`
- `head`

Command:

```bash
tr -cs '[:alpha:]' '\n' < pg1661.txt \
| tr '[:upper:]' '[:lower:]' \
| sort \
| uniq -c \
| sort -nr \
| head
```

The pipeline:

1. Converts non-alphabetic characters into newlines to separate words.
2. Converts uppercase characters to lowercase.
3. Sorts the words alphabetically.
4. Counts repeated words using `uniq -c`.
5. Sorts the counts in descending numerical order.
6. Displays the top 10 results using `head`.

---
<img width="1390" height="538" alt="Screenshot From 2026-08-09 15-59-25" src="https://github.com/user-attachments/assets/7bb2b978-840c-4590-bbb6-ad1decd09ed8" />


### 3. Counted Lines, Words, and Characters

Used the `wc` command to inspect the text files.

```bash
wc pg1661.txt
```

Individual counts can also be obtained using:

```bash
wc -l pg1661.txt
wc -w pg1661.txt
wc -c pg1661.txt
```

Where:

- `-l` → lines
- `-w` → words
- `-c` → characters/bytes

---
<img width="787" height="58" alt="Screenshot From 2026-08-09 15-59-59" src="https://github.com/user-attachments/assets/066d38d4-c444-4239-98fa-970d67cf0b04" />



### 4. Created `top_words.sh`

Created a parameterized Bash script that accepts:

- A required filename as the first argument.
- An optional number of words as the second argument.
- Defaults to 10 words if the second argument is not provided.

```bash
#!/bin/bash

File=$1
count=${2:-10}

tr -cs '[:alpha:]' '\n' < "$File" \
| tr '[:upper:]' '[:lower:]' \
| sort \
| uniq -c \
| sort -nr \
| head -n "$count"
```

Example:

```bash
./top_words.sh pg1661.txt
```

This prints the top 10 most frequent words.

To print a custom number:

```bash
./top_words.sh pg1661.txt 15
```

This prints the top 15 most frequent words.

---
<img width="560" height="356" alt="Screenshot From 2026-08-09 15-48-00" src="https://github.com/user-attachments/assets/f56ab68b-e9aa-4e9e-bad3-771fba5b4039" />


### 5. Made the Script Executable

Changed the file permissions using:

```bash
chmod +x top_words.sh
```
<img width="1331" height="533" alt="Screenshot From 2026-08-09 16-04-48" src="https://github.com/user-attachments/assets/4f47af2c-d5b6-4cc2-b29f-b4788f5a9358" />

The script was then executed on two different text files:

```bash
./top_words.sh pg1661.txt
```

```bash
./top_words.sh pg45839.txt
```

Custom counts were also tested:

```bash
./top_words.sh pg45839.txt 15
```

---
<img width="860" height="148" alt="Screenshot From 2026-08-09 16-02-17" src="https://github.com/user-attachments/assets/f6226634-41a9-4376-ac83-a0a9b271b254" />

## Commands and Concepts Covered

- `curl`
- `wc`
- `tr`
- `sort`
- `uniq`
- `head`
- Bash variables
- Command-line arguments (`$1`, `$2`)
- Default parameter values (`${2:-10}`)
- Pipelines (`|`)
- Input redirection (`<`)
- File permissions
- `chmod +x`
- Bash scripting

---

## Project Structure

```text
lab4/
├── pg1661.txt
├── pg45839.txt
├── top_words.sh
└── README.md
```

---

## Learning Outcomes

After completing this lab, I learned how to:

- Navigate and work with files using the Linux command line.
- Download files using `curl`.
- Count lines, words, and characters using `wc`.
- Process text using `tr`, `sort`, and `uniq`.
- Combine multiple commands using pipelines.
- Write a parameterized Bash script.
- Use command-line arguments in Bash.
- Provide default values for optional arguments.
- Make a Bash script executable using `chmod +x`.
- Run the same script on different input files.
