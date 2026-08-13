# Matplotlib

## 1. Objective

The objective of this topic is to understand the fundamentals of Matplotlib and learn how to create, customize, interpret, and save different types of visualizations in Python.

By the end of this topic, I should be able to:

* Create basic plots using Matplotlib.
* Understand the role of x-axis and y-axis.
* Add titles, labels, legends, and grids.
* Customize plots using markers, colors, and line styles.
* Create multiple plots in a single figure.
* Use different types of charts for different types of data.
* Control the appearance of axes.
* Save plots as image files.
* Select an appropriate visualization based on the data and the purpose of analysis.

---

## 2. What is Matplotlib?

Matplotlib is a Python library used to create data visualizations.

It allows us to represent numerical and categorical data using graphs and charts.

Some commonly used visualizations in Matplotlib are:

* Line plots
* Bar charts
* Scatter plots
* Histograms
* Pie charts
* Boxplots

Visualization makes it easier to identify patterns, trends, comparisons, distributions, and relationships in data.

---

## 3. Importing Matplotlib

The commonly used module for creating plots is `pyplot`.

```python
import matplotlib.pyplot as plt
```

`plt` is an alias for `matplotlib.pyplot` and makes the code shorter and easier to write.

---

## 4. Basic Line Plot

A line plot can be created using `plt.plot()`.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

Here:

* `x` contains the values plotted on the x-axis.
* `y` contains the corresponding values plotted on the y-axis.
* `plt.plot(x, y)` creates the line plot.
* `plt.show()` displays the plot.

The corresponding points are:

```text
(1, 2)
(2, 4)
(3, 6)
(4, 8)
(5, 10)
```

The points are connected by a line.

### Important

`plt.plot()` creates the plot, while `plt.show()` displays it.

---

## 5. Adding Labels and Title

A graph should have meaningful labels and a title so that it can be understood without looking at the code.

```python
plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Relationship between X and Y")

plt.show()
```

### Functions

| Function       | Purpose                    |
| -------------- | -------------------------- |
| `plt.xlabel()` | Sets the x-axis label      |
| `plt.ylabel()` | Sets the y-axis label      |
| `plt.title()`  | Sets the title of the plot |

Labels describe what the axes represent, while the title describes what the overall graph represents.

---

## 6. Customizing a Line Plot

Matplotlib allows us to customize the appearance of a plot.

```python
plt.plot(
    x,
    y,
    marker="o",
    linestyle="--",
    color="red"
)

plt.show()
```

### Common parameters

#### Marker

```python
marker="o"
```

Displays a marker at each data point.

#### Line style

```python
linestyle="--"
```

Makes the line dashed.

#### Color

```python
color="red"
```

Changes the color of the line.

These parameters only change the visual appearance of the graph. They do not change the underlying data.

---

## 7. Figure Size

The size of a figure can be controlled using `figsize`.

```python
plt.figure(figsize=(8, 5))
```

The first value represents the width and the second represents the height.

```python
figsize=(width, height)
```

The values are specified in inches.

Changing the figure size changes the display area but does not change the underlying data.

---

## 8. Grid

A grid can make values easier to read from a graph.

```python
plt.grid(True)
```

To remove the grid:

```python
plt.grid(False)
```

The grid is mainly a readability feature and does not affect the data.

---

## 9. Multiple Lines on the Same Plot

Multiple datasets can be plotted on the same figure.

```python
x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, marker="o", label="Line 1")
plt.plot(x, y2, marker="s", label="Line 2")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Comparison of Two Lines")

plt.legend()
plt.grid(True)

plt.show()
```

### `label`

The `label` parameter gives a name to a plotted line.

### `plt.legend()`

`plt.legend()` displays the labels on the graph so that the different lines can be identified.

---

## 10. Subplots

Sometimes multiple graphs need to be displayed within a single figure.

The `subplot()` function divides a figure into multiple areas.

```python
plt.subplot(rows, columns, position)
```

For example:

```python
plt.subplot(1, 2, 1)
```

means:

* `1` row
* `2` columns
* position `1`

The layout becomes:

```text
┌──────────────┬──────────────┐
│  Position 1  │  Position 2  │
└──────────────┴──────────────┘
```

Similarly:

```python
plt.subplot(2, 1, 1)
```

creates 2 rows and 1 column.

```text
┌──────────────┐
│  Position 1  │
├──────────────┤
│  Position 2  │
└──────────────┘
```

### `plt.tight_layout()`

```python
plt.tight_layout()
```

Automatically adjusts spacing between plots so that titles and labels do not overlap.

---

## 11. Bar Chart

A bar chart is useful for comparing values across different categories.

```python
categories = ["Python", "SQL", "Java", "C++"]
values = [90, 80, 70, 60]

plt.bar(categories, values)

plt.xlabel("Skills")
plt.ylabel("Score")
plt.title("Skill-wise Score")

plt.show()
```

Here:

* Categories are represented on the x-axis.
* Their corresponding values determine the height of the bars.

### When to use a bar chart?

Bar charts are useful when comparing values across discrete categories.

For example:

* Sales by product
* Marks by student
* Number of employees by department
* Skill scores

---

## 12. Horizontal Bar Chart

A horizontal bar chart can be created using `barh()`.

```python
plt.barh(categories, values)

plt.xlabel("Score")
plt.ylabel("Skills")
plt.title("Skill-wise Score")

plt.show()
```

Difference:

```python
plt.bar()
```

creates vertical bars.

```python
plt.barh()
```

creates horizontal bars.

Horizontal bars can be more readable when category names are long.

---

## 13. Scatter Plot

A scatter plot represents individual observations as points.

```python
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 8, 9, 12]

plt.scatter(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Relationship between X and Y")

plt.show()
```

Unlike a line plot, a scatter plot does not connect the points with a line.

### Why use a scatter plot?

It is useful for examining the relationship between two numerical variables.

Examples:

* Hours studied vs exam score
* Height vs weight
* Advertising expenditure vs sales

Scatter plots will be useful later when studying correlation.

---

## 14. Histogram

A histogram shows the distribution of numerical data by grouping values into intervals called bins.

```python
data = [
    10, 12, 12, 13, 14, 14, 14, 15, 16, 17,
    18, 18, 19, 20, 21, 22, 22, 23, 24, 25
]

plt.hist(data)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Distribution of Values")

plt.show()
```

The bars represent how many observations fall within each interval.

### Bins

The number of bins can be controlled:

```python
plt.hist(data, bins=5)
```

or:

```python
plt.hist(data, bins=10)
```

Changing the number of bins changes how the data is grouped and therefore changes the appearance of the histogram.

### Histogram vs Bar Chart

A bar chart generally compares categories:

```text
Category → Value
```

A histogram shows the distribution of numerical data:

```text
Numerical values → Intervals → Frequency
```

---

## 15. Pie Chart

A pie chart represents parts of a whole.

```python
categories = ["Python", "SQL", "Java", "C++"]
values = [40, 30, 20, 10]

plt.pie(
    values,
    labels=categories
)

plt.title("Skill Distribution")

plt.show()
```

The total value is:

```text
40 + 30 + 20 + 10 = 100
```

Therefore, the slices represent the proportion of each category.

### Displaying percentages

```python
plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%"
)

plt.show()
```

`autopct` controls how percentages are displayed inside the pie chart.

### When to use a pie chart?

Pie charts are useful when:

* Categories represent parts of one whole.
* There are relatively few categories.
* The proportions are more important than exact comparisons.

For many categories, a bar chart is usually easier to interpret.

---

## 16. Boxplot

A boxplot is used to summarize the distribution of numerical data and can help identify potential outliers.

```python
data = [
    10, 12, 13, 14, 15, 15, 16,
    17, 18, 20, 22, 25, 30
]

plt.boxplot(data)

plt.ylabel("Values")
plt.title("Distribution of Data")

plt.show()
```

A boxplot visually represents important points in a distribution, including:

* Median
* Lower quartile
* Upper quartile
* Whiskers
* Potential outliers

The detailed meaning of quartiles and IQR will be covered separately in the statistics section.

### Why is boxplot important?

Boxplots are useful for:

* Understanding spread
* Comparing distributions
* Identifying potential outliers
* Summarizing numerical data

---

## 17. Controlling Axis Limits

The visible range of an axis can be controlled using `xlim()` and `ylim()`.

```python
plt.xlim(0, 6)
plt.ylim(0, 12)
```

`xlim()` controls the visible x-axis range.

`ylim()` controls the visible y-axis range.

These functions change the visible range of the graph, not the underlying data.

---

## 18. Customizing Axis Ticks

Ticks are the positions shown along an axis.

For example:

```python
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10])
```

We can also replace numerical tick labels with meaningful names:

```python
plt.xticks(
    [1, 2, 3, 4],
    ["Python", "SQL", "Java", "C++"]
)
```

### Difference between limits and ticks

```text
xlim / ylim
    ↓
Controls the visible range

xticks / yticks
    ↓
Controls tick positions and labels
```

---

## 19. Figure and Axes

A more structured way of working with Matplotlib is:

```python
fig, ax = plt.subplots()
```

This creates two objects:

* `fig` → the complete figure
* `ax` → the actual plotting area (axes)

Example:

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y, marker="o")

ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Relationship between X and Y")

ax.grid(True)

plt.show()
```

Instead of directly using:

```python
plt.plot()
plt.xlabel()
plt.ylabel()
```

we can operate directly on the axes:

```python
ax.plot()
ax.set_xlabel()
ax.set_ylabel()
ax.set_title()
ax.grid()
```

This approach becomes especially useful when working with multiple plots.

---

## 20. Multiple Axes using `plt.subplots()`

Multiple plots can be created using:

```python
fig, axes = plt.subplots(1, 2)
```

This creates:

```text
┌──────────────┬──────────────┐
│   axes[0]    │   axes[1]    │
└──────────────┴──────────────┘
```

Example:

```python
x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [10, 8, 6, 4, 2]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y1, marker="o")
axes[0].set_title("Increasing")

axes[1].plot(x, y2, marker="s")
axes[1].set_title("Decreasing")

plt.tight_layout()

plt.show()
```

For a `2 × 2` layout:

```python
fig, axes = plt.subplots(2, 2)
```

The axes can be accessed as:

```python
axes[0, 0]
axes[0, 1]
axes[1, 0]
axes[1, 1]
```

This is useful when several related visualizations need to be compared.

---

## 21. Saving a Plot

A plot can be saved using `savefig()`.

```python
fig, ax = plt.subplots()

ax.plot(x, y)

fig.savefig("multiple_plot.png")

plt.show()
```

The graph is saved as:

```text
multiple_plot.png
```



```python
fig.savefig("multiple_plot.png")
```

Matplotlib can save plots in different formats such as:

* PNG
* JPG
* PDF

---

## 22. Practical Implementation

The concepts above were practically implemented using Python and Matplotlib.

Example:

```python
import matplotlib.pyplot as plt

students = ["Aman", "Rahul", "Jatin", "Priya", "Neha"]
marks = [65, 80, 72, 90, 55]

fig, ax = plt.subplots()

ax.bar(students, marks)

ax.set_xlabel("Students")
ax.set_ylabel("Marks")
ax.set_title("Class Marks Report")

ax.grid(True)

fig.savefig("student_marks.png")

plt.show()
```

This practical implementation demonstrates:

* Creating categorical data
* Creating a bar chart
* Adding axis labels
* Adding a title
* Adding a grid
* Creating a figure and axes
* Saving the final graph as an image

---

## 23. What I Understood

Matplotlib is a visualization library that allows numerical and categorical data to be represented graphically.

The main thing I understood is that different plots serve different analytical purposes rather than being interchangeable.

I learned how to:

* Create basic line plots.
* Add titles and axis labels.
* Customize markers, line styles, colors, and grids.
* Plot multiple datasets.
* Create subplots.
* Create bar and horizontal bar charts.
* Create scatter plots.
* Create histograms.
* Create pie charts.
* Create boxplots.
* Control axis limits and ticks.
* Work with `fig` and `ax`.
* Save visualizations as image files.

I also understood that visualization is useful not only for making data look better, but for identifying patterns, comparisons, distributions, relationships, and potential outliers.

---
