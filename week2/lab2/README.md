# Lab 2 – NumPy and Vectorization

## Objective

The objective of this lab is to understand NumPy arrays, vectorized operations, broadcasting, normalization, and the performance difference between Python loops and NumPy vectorization.

## Tasks Performed

### 1. 2D NumPy Array Operations

Created a 2D NumPy array and performed:

* Row-wise mean calculation using `axis=1`
* Column-wise maximum calculation using `axis=0`

```python
row_means = data.mean(axis=1)
column_maxima = data.max(axis=0)
```

### 2. Column-wise Normalization

Normalized each column to a range between 0 and 1 using:

```text
normalized = (x - min) / (max - min)
```

Implementation:

```python
column_min = data.min(axis=0)
column_max = data.max(axis=0)

normalized_data = (data - column_min) / (column_max - column_min)
```

### 3. Broadcasting

Calculated the mean of each column and subtracted it from the complete dataset using NumPy broadcasting.

```python
column_means = data.mean(axis=0)
centered_data = data - column_means
```

Broadcasting allows NumPy to perform operations between arrays with compatible shapes without explicitly repeating the smaller array.

### 4. Vectorization vs Python Loop

Compared the execution time of:

* A traditional Python `for` loop
* A NumPy vectorized operation

Example vectorized operation:

```python
vectorized_result = large_data * 2
```

Execution time was measured using Python's `time` module.

## Key Concepts

* NumPy 2D arrays
* `axis=0` and `axis=1`
* Row-wise and column-wise operations
* Min-Max normalization
* Broadcasting
* Vectorization
* Performance comparison
* Execution time measurement

## Requirements

* Python 3.x
* NumPy

Install NumPy using:

```bash
pip install numpy
```

## How to Run

Run the Python script or Jupyter Notebook containing the lab code:

```bash
python lab2.py
```

The program displays the original data, row means, column maxima, normalized data, centered data, and execution times for loop-based and vectorized operations.

## Conclusion

This lab demonstrates how NumPy can simplify numerical operations on arrays. Broadcasting allows operations between compatible array shapes, while vectorization eliminates explicit Python loops and generally provides better performance for large numerical datasets.
