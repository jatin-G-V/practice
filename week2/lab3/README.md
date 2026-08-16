# Lab 3 – Data Cleaning with Pandas

## Objective

The objective of this lab is to clean and validate a messy employee dataset using Pandas. The dataset contains missing values, invalid values, inconsistent data types, duplicate records, an invalid date, and an outlier.

## Dataset

Input file:

```text
messy data.csv
```

The dataset contains the following columns:

* `Employee_ID`
* `Name`
* `Age`
* `Department`
* `Salary`
* `Joining_Date`
* `Experience_Years`
* `Performance_Score`

## Data Cleaning Steps

### 1. Missing Value Analysis

Missing values were identified using:

```python
df.isnull().sum()
```

Both the missing count and missing percentage were calculated for each column.

```python
missing_summary = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": (df.isnull().sum() / len(df)) * 100
})
```

### 2. Handling Incorrect Data Types

The `Salary` column contained the value `"not available"`, which caused Pandas to treat the column as a non-numeric type.

It was converted to numeric using:

```python
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
```

The `Age` column contained `"thirty"`, so it was also converted to numeric:

```python
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
```

Invalid non-numeric values were converted to `NaN`.

### 3. Missing Numerical Values

Missing numerical values were handled using median imputation.

The median was chosen instead of the mean because the dataset contains potential outliers, and the median is less affected by extreme values.

Columns handled:

* `Salary`
* `Age`
* `Experience_Years`
* `Performance_Score`

Example:

```python
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
```

### 4. Duplicate Records

Duplicate records were checked while ignoring `Employee_ID`, because the same employee information could appear with a different ID.

```python
duplicate_columns = [
    "Name",
    "Age",
    "Department",
    "Salary",
    "Joining_Date",
    "Experience_Years",
    "Performance_Score"
]

df = df.drop_duplicates(subset=duplicate_columns)
```

The duplicate employee record was removed while keeping the first occurrence.

### 5. Handling Invalid Values

Some values were logically invalid.

#### Invalid Age

An age of `150` was treated as invalid:

```python
df.loc[df["Age"] > 100, "Age"] = np.nan
```

The resulting missing value was then replaced with the median age.

#### Invalid Experience

An experience value of `-2` was treated as invalid:

```python
df.loc[df["Experience_Years"] < 0, "Experience_Years"] = np.nan
```

It was then replaced with the median experience.

### 6. Handling Salary Outliers

The IQR method was used to identify salary outliers.

```python
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```

The salary of `500000` was treated as an obvious outlier and replaced with the median salary because it was substantially inconsistent with the other salary values.

The `76000` salary was retained because it was considered plausible despite being flagged by the IQR method.

### 7. Date Cleaning

The `Joining_Date` column contained multiple date formats and one invalid date.

The column was converted to datetime:

```python
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    dayfirst=True,
    errors="coerce"
)
```

The invalid date `31/13/2023` was converted to `NaT`.

The invalid date was left as `NaT` because the correct joining date could not be determined from the available data. Assigning an arbitrary date would introduce incorrect information.

### 8. Department Standardization

Department names were standardized to uppercase to handle inconsistent values such as `IT` and `it`.

```python
df["Department"] = df["Department"].str.strip().str.upper()
```

This results in consistent department values such as:

```text
IT
HR
SALES
FINANCE
```

## Final Validation

After cleaning, the dataset was validated by checking:

* Missing values
* Data types
* Duplicate records
* Invalid ages
* Invalid experience values
* Salary outliers
* Final number of rows and columns

The cleaned dataset contains **25 rows and 8 columns**.

The invalid joining date remains as `NaT` because its correct value could not be determined.

## Exporting the Cleaned Dataset

The cleaned dataset was saved as:

```python
df.to_csv("cleaned_data.csv", index=False)
```

Output file:

```text
cleaned_data.csv
```

## Requirements

* Python 3.x
* Pandas
* NumPy

Install the required libraries:

```bash
pip install pandas numpy
```

## How to Run

Run the Jupyter Notebook containing the cleaning operations, or execute the Python script containing the same code.

The cleaned dataset will be generated as:

```text
cleaned_data.csv
```

## Conclusion

This lab demonstrates practical data cleaning using Pandas. Missing values were analyzed and handled, incorrect data types were converted, invalid values were identified and corrected, duplicate records were removed, an obvious salary outlier was treated, dates were standardized, and categorical values were made consistent. The final dataset was validated and exported as a cleaned CSV file.
