# Lab 5 – Visualization and Mini-EDA

## Objective

To visualize and communicate patterns in the cleaned employee dataset using charts and perform a quick exploratory data analysis (EDA).

## Dataset

The cleaned employee dataset was used for visualization and analysis.

### Columns Used

* Age
* Salary
* Department
* Joining_Date

## Tasks Performed

### 1. Histogram and Boxplot

A histogram was created for the `Salary` column to visualize the salary distribution.

A boxplot was created to understand the spread of salaries, median, and potential outliers.

**Observation:** Most employee salaries are concentrated between ₹45,000 and ₹60,000, while a few higher salaries extend the distribution toward the right.

### 2. Scatter Plot

A scatter plot of `Age` versus `Salary` was created to visualize their relationship.

**Observation:** The scatter plot shows a strong positive relationship between Age and Salary, where salary generally increases as employee age increases.

### 3. Correlation Heatmap

A correlation heatmap was created using Seaborn.

The correlation between Age and Salary was approximately **0.72**, indicating a strong positive correlation.

### 4. Mini-EDA

A quick end-to-end analysis was performed by checking:

* Dataset shape
* Missing values
* Summary statistics
* Average salary by department

**Observations:**

1. The dataset contains 25 employees and 6 columns.
2. Age has 1 missing value and Joining_Date has 3 missing values, while the other columns have no missing values.
3. Finance has the highest average salary among the departments.

## Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Conclusion

The visualization and mini-EDA helped identify salary distribution, potential outliers, the relationship between age and salary, and department-wise salary patterns in the cleaned dataset.
