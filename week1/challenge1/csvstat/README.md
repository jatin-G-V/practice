# CSVStat

CSVStat is a command-line CSV analysis tool built using Python's standard library.

The tool reads a CSV file provided through the command line and generates useful information about the dataset, including its structure, data types, numeric statistics, frequent values, and missing values.

The project is implemented without using external data-analysis libraries such as Pandas or NumPy.

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
* Retrieve values from a particular column
* Extract numeric values from a column
* Calculate minimum, maximum, and mean for a numeric column
* Calculate minimum, maximum, and mean for all numeric columns
* Find the most frequent values of a particular column
* Find the most frequent values of all columns
* Count missing values
* Calculate the percentage of missing values
* Accept a configurable `--top` argument
* Handle missing files
* Validate the CSV file extension
* Use reusable helper functions to avoid repeated CSV parsing logic
* Follow the DRY (Don't Repeat Yourself) principle for numeric statistics

---

# Functions

The main functions implemented in `csvstat.py` are:

```text
csvstat.py
│
├── number_Of_Rows()
├── number_Of_Columns()
├── value_type()
├── columns()
├── column_values()
├── numeric_column_values()
├── column_type()
├── table_info()
│
├── numeric_stats()
├── numeric_columns_stats()
│
├── most_frequent_values()
├── frequent_values_all_columns()
│
├── missing_values()
│
└── main()
```

### Numeric Statistics Flow

Numeric statistics use reusable helper functions to avoid duplicating CSV parsing and numeric conversion logic:

```text
column_values()
       │
       ▼
numeric_column_values()
       │
       ▼
numeric_stats()
       │
       ├── min
       ├── max
       └── mean
```

This structure keeps the code easier to maintain and makes the numeric-statistics logic easier for other developers and interns to understand.

---

# Usage

Run CSVStat from the command line by providing the CSV file path:

```bash
python3 csvstat.py <csv_file>
```

The `--top` argument can be used to control how many frequent values are displayed.

For example:

```bash
python3 csvstat.py winequality.csv --top 2
```

If `--top` is not provided, the default value is `5`.

---

# Sample Output

### Using the default value of `--top`

<img width="1402" height="396" alt="image" src="https://github.com/user-attachments/assets/c0cec3b3-7f62-4196-89f9-74f9866cc642" />

### Assigning the value `2` to `--top`

<img width="1400" height="368" alt="image" src="https://github.com/user-attachments/assets/bb7c4cfe-2c54-4d0d-8471-95387af637f2" />


---

# Requirements

* Python 3.x
* No external Python packages are required

The project uses only Python's standard library.

### Standard Library Modules

```python
import argparse
from datetime import datetime
```

---

# Design Principles

### DRY — Don't Repeat Yourself

The numeric statistics implementation was refactored to avoid repeating the same CSV parsing, column extraction, and numeric conversion logic across separate functions.

Instead of maintaining separate implementations for minimum, maximum, and mean calculations, CSV values are extracted and converted once through reusable helper functions.

This makes the code:

* Easier to maintain
* Easier to understand
* Less repetitive
* Easier for other interns to study and extend
