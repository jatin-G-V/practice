# Week 2 — Titanic Dataset EDA

## Overview

This project is a complete Exploratory Data Analysis (EDA) of the Titanic dataset.

The objective is to analyze a messy real-world dataset and answer three key questions:

- What is in the data?
- What can be trusted?
- What are the three most important things to know?

The analysis includes data profiling, cleaning, exploratory analysis, visualizations, key insights, and data-quality/modeling risks.

---

## Dataset

The Titanic dataset was obtained from the Kaggle Titanic competition.

Dataset source:

https://www.kaggle.com/c/titanic/data

The dataset contains passenger information such as age, sex, passenger class, fare, family relationships, ticket information, and survival status.

The raw dataset is stored locally in the `data/` directory and is not committed to the repository.

---

## Repository Structure

```text
week2-eda/
│
├── README.md
├── requirements.txt
├── .gitignore
├── eda.ipynb
├── summary.md
│
└── data/
    └── train.csv
```
## Analysis Workflow

Load and profile the raw dataset

Analyze column types and missingness

Check for duplicate records

Investigate potential outliers

Clean the dataset with documented rationales

Validate the cleaned dataset

Explore important relationships using visualizations

Extract three key insights

Identify data-quality and modeling risks

Prepare a one-page stakeholder summary

## Conclusion
This analysis demonstrates the complete workflow of taking a messy dataset from raw profiling through cleaning and exploratory analysis to clear, actionable findings while explicitly documenting uncertainty and data-quality risks.
