# Lab 1 – Pandas Fundamentals

## Objective

The objective of this lab is to practice basic Pandas operations for working with tabular data.

## Dataset

**Dataset:** Red Wine Quality Dataset

The dataset contains information about different properties of red wine along with its quality score.

* Rows: 1143
* Columns: 13

## Requirements

* Python 3.x
* Pandas

Install Pandas using:

```bash
pip install pandas
```

## Tasks Performed

### 1. Load and Inspect the Dataset

The CSV file is loaded into a Pandas DataFrame and inspected using:

* `head()` – displays the first few rows
* `info()` – displays column information and data types
* `describe()` – provides statistical summary
* `shape` – returns the number of rows and columns

```python
import pandas as pd

df = pd.read_csv("winequality-red.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
```

### 2. Select Rows and Columns

Pandas `loc` and `iloc` are used to select specific rows and columns.

Boolean filtering is also used to filter records based on conditions.

```python
df.loc[:, ["alcohol", "quality"]]

df.iloc[0:5, 0:3]

df[df["alcohol"] > 12]

df.loc[df["alcohol"] > 12, ["alcohol", "quality"]]
```

### 3. Create a New Column

A new column is created using existing columns.

```python
df["sulfur_ratio"] = (
    df["free sulfur dioxide"] /
    df["total sulfur dioxide"]
)
```

The new column represents the ratio between free sulfur dioxide and total sulfur dioxide.

### 4. GroupBy and Aggregation

The data is grouped by `quality` and the `alcohol` column is aggregated using `mean` and `count`.

```python
quality_summary = df.groupby("quality")["alcohol"].agg(
    mean_alcohol="mean",
    wine_count="count"
)

print(quality_summary)
```

This provides the average alcohol content and number of records for each quality level.

### 5. Merge Two DataFrames

Two DataFrames are created from the original dataset and merged using the common `Id` column.

```python
df1 = df[["Id", "quality"]].copy()
df2 = df[["Id", "alcohol"]].copy()

merged_df = pd.merge(df1, df2, on="Id")

print(merged_df.head())

print("Original rows:", len(df))
print("Merged rows:", len(merged_df))
```

The resulting row count is checked to verify that the merge produced the expected number of records.

## Conclusion

This lab demonstrates the basic use of Pandas for:

* Loading CSV data
* Inspecting DataFrames
* Selecting rows and columns
* Filtering data
* Creating derived columns
* Grouping and aggregating data
* Merging DataFrames
* Verifying row counts
