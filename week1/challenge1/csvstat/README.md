# CSVStat

CSVStat is a command-line CSV analysis tool built using Python's standard library.

The tool reads a CSV file provided through the command line and generates useful information about the dataset, including its structure, data types, numeric statistics, frequent values, and missing values.

The project was implemented without using external data-analysis libraries such as Pandas or NumPy.

---

## Features

CSVStat currently supports the following operations:

* Count the number of rows in a CSV file
* Count the number of columns
* Detect basic data types:

  * `int`
  * `float`
  * `date`
  * `str`
* Display column names and their detected types
* Find the minimum value of a numeric column
* Find the maximum value of a numeric column
* Calculate the mean of a numeric column
* Calculate mean for all numeric columns
* Calculate minimum for all numeric columns
* Calculate maximum for all numeric columns
* Find the most frequent values of a particular column
* Find the most frequent values of all text columns
* Count missing values
* Calculate the percentage of missing values
* Accept a configurable `--top` argument
* Handle missing files
* Validate the CSV file extension
* Perform operations on individual columns through reusable functions

---

# Functions List

```text
csvstat.py
│
├── rows()
├── columns()
├── table_info()
├── value_type()
├── column_type()
│
├── column_min()
├── column_max()
├── column_mean()
│
├── numeric_columns_mean()
├── numeric_columns_min()
├── numeric_columns_max()
│
├── most_frequent_values()
├── frequent_values_all_columns()
│
├── missing_values()
│
└── main()
```

---

# Sample Output

### Using the default value of `--top`

<img width="1540" height="425" alt="Screenshot From 2026-08-11 01-57-51" src="https://github.com/user-attachments/assets/9f901185-6017-4529-a3df-c9097261f583" />

### Assigning the value `2` to `--top`

<img width="1556" height="392" alt="image" src="https://github.com/user-attachments/assets/47ed05b8-037d-4b41-bafc-262f2295134a" />

# Requirements

* Python 3.x
* No external Python packages are required

The project uses Python's standard library.

### Standard Library Modules

```python
import argparse
from datetime import datetime
```
