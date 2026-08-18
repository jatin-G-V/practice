# Titanic EDA — Executive Summary

## The Three Things to Know

### 1. Sex and passenger class jointly shaped survival

Survival differed substantially across both sex and passenger class. Female passengers had much higher survival rates than male passengers within each class, while survival also generally decreased from first class to third class. Looking at sex and passenger class together therefore gives a clearer picture of survival than considering either variable alone.

### 2. Age was not a strong separator of survival

Survivors and non-survivors had the same median age of 28 years and substantially overlapping age distributions. Survivors were slightly younger on average, but the difference was small compared with the overall variation in age. Age alone therefore did not clearly distinguish survivors from non-survivors.

### 3. Higher fares were associated with higher survival

Survivors generally paid higher fares than non-survivors. At the extreme end, all three passengers with the maximum recorded fare of 512.3292 survived, while survival among zero-fare passengers was extremely uncommon. However, these extreme groups are very small, and the relationship may partly reflect differences in passenger class rather than fare itself.

## Data Quality and Modeling Risks

- **Ticket/Fare inconsistency:** Ticket `7534` appears with two different Fare values (9.2167 and 9.8458). This should be investigated before using Ticket and Fare together for feature engineering or modeling.
- **Missing Age:** 177 missing Age values were replaced with the median age of 28. This preserves the records but may slightly affect the observed age distribution.
- **Target leakage:** `Survived` is the target variable and must not be included as a model feature.
- **Cabin missingness:** Approximately 77% of Cabin values were missing, so the Cabin column was dropped rather than filled with unreliable values.

## Actionable Takeaway

Passenger class and sex show the clearest differences in survival in this dataset, while age provides a much weaker separation. Fare also shows a strong association with survival, but this should be interpreted alongside passenger class rather than as an independent causal factor. Before modeling, the Ticket/Fare inconsistency and effects of missing-value treatment should be reviewed, and the target variable must be kept separate from model inputs.