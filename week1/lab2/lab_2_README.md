# Lab 2 – Python Functions

## Objective

The objective of this lab is to understand Python functions, dictionaries, list comprehensions, generators, file handling, and exception handling by implementing practical programs.

---

## Tasks Performed

### 1. Word Count (Manual Implementation)

Implemented a `word_count(text)` function that:

- Converts the input text to lowercase.
- Removes punctuation marks.
- Counts the frequency of each word using a dictionary.
- Returns the word-frequency dictionary.

---

<img width="1330" height="797" alt="Screenshot From 2026-08-06 12-27-53" src="https://github.com/user-attachments/assets/62ccf7de-564f-4739-99cb-a7e74d4f76db" />


### 2. Word Count using `collections.Counter`

Implemented another version of the word count using Python's built-in `collections.Counter` module.

Both implementations were tested to verify that they produce identical results.

---
<img width="1400" height="792" alt="Screenshot From 2026-08-06 12-41-08" src="https://github.com/user-attachments/assets/aba59e98-f4e5-48d2-b3ec-bddf5e15502f" />

### 3. Flatten Nested Lists

Implemented two versions of a function to flatten a nested list.

- Using nested `for` loops.
- Using list comprehension.

Example:

Input

```python
[[1, 2], [3, 4], [5]]
```

Output

```python
[1, 2, 3, 4, 5]
```

---
<img width="1400" height="792" alt="Screenshot From 2026-08-06 12-51-01" src="https://github.com/user-attachments/assets/c13e8c84-0047-48a4-811c-413f2a5c159e" />

### 4. Mean of Numbers in a File

Implemented `mean_of_file(path)` which:

- Opens a text file.
- Reads one number per line.
- Calculates the arithmetic mean of valid numbers.
- Skips invalid entries using exception handling.
- Handles missing files gracefully using `FileNotFoundError`.

Example file:

```text
34
23
67
abs
54
78
```

Output:

```text
51.2
```

---
<img width="1531" height="872" alt="Screenshot From 2026-08-06 13-34-25" src="https://github.com/user-attachments/assets/3fe1a26d-d1dd-4114-b79d-9b17b256702e" />

### 5. List Comprehension vs Generator Expression

Demonstrated the difference between:

- List Comprehension
- Generator Expression

#### List Comprehension

- Creates the complete list immediately.
- Faster for small datasets.
- Uses more memory.

#### Generator Expression

- Produces values one at a time.
- Uses significantly less memory.
- Suitable for processing large datasets.

---
<img width="1375" height="773" alt="Screenshot From 2026-08-06 13-46-56" src="https://github.com/user-attachments/assets/4dacffd1-e144-480a-bc2f-0b665e7616d0" />

### 6. Testing using `__main__`

Created a `main()` function to test every implemented function.

---
<img width="1388" height="792" alt="Screenshot From 2026-08-06 14-02-20" src="https://github.com/user-attachments/assets/99d9398e-f298-47e6-a267-e5ffb499624a" />

Used

```python
if __name__ == "__main__":
    main()
```

to ensure that the test code executes only when the file is run directly and not when it is imported as a module.

---
<img width="1255" height="650" alt="Screenshot From 2026-08-06 14-04-13" src="https://github.com/user-attachments/assets/52c16417-cdc4-49c2-b0e1-e3a96d1cf733" />


---
## Project Structure

```
lab2/
│── alpha.txt
│── hello.py
│── numbers.txt
│── lab_2_README.md
```

---
## Learning Outcomes

After completing this lab, I learned how to:

- Write reusable Python functions.
- Count word frequencies using both dictionaries and `collections.Counter`.
- Flatten nested lists using loops and list comprehensions.
- Read data from files and calculate statistics.
- Handle runtime errors using exception handling.
- Understand the memory difference between list comprehensions and generators.
- Use the `if __name__ == "__main__"` block to organize and test Python programs.
