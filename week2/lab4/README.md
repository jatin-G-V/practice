# Lab 4 – Statistics Intuition

## Objective

To understand basic statistical concepts and apply them to employee salary data using Python, Pandas, NumPy, Matplotlib, and SciPy.

## Dataset

The cleaned employee dataset was used for the analysis.

### Columns Used

* Age
* Salary
* Department

## Tasks Performed

### 1. Descriptive Statistics

Calculated:

* Mean
* Median
* Standard Deviation
* 25th, 50th, and 75th Percentiles

**Results:**

* Mean Salary: ₹54,720
* Median Salary: ₹53,500
* Standard Deviation: ₹8,361.72
* 25th Percentile: ₹49,500
* 50th Percentile: ₹53,500
* 75th Percentile: ₹58,000

### 2. Distribution, Skewness and Outliers

A histogram was used to visualize the salary distribution.

The calculated skewness was **0.9733**, indicating that the salary distribution is **right-skewed**.

The IQR method was used to identify potential salary outliers.

### 3. Correlation Analysis

A correlation matrix was created for Age and Salary.

The correlation between Age and Salary was:

**0.7186**

This indicates a strong positive correlation. However, correlation does not imply causation.

### 4. Hypothesis Testing

An independent two-sample t-test was performed to compare the salaries of HR and Sales employees.

**Results:**

* T-statistic: 0.0036
* P-value: 0.9972

Since the p-value is greater than 0.05, the null hypothesis was not rejected. Therefore, there was no statistically significant difference between the average salaries of HR and Sales employees in this dataset.

## Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
```

## Conclusion

The analysis provided an understanding of descriptive statistics, salary distribution, skewness, outliers, correlation, and hypothesis testing using the employee dataset.
