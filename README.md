# A/B Test for Delivery App

A data analysis project investigating whether a redesigned food delivery application interface increases the **Average Order Value (AOV)** using statistical hypothesis testing.

## Overview

This project simulates an end-to-end A/B testing workflow, beginning with validating sample quality and concluding with statistical analysis of the experiment results. The analysis follows common industry practices, including power analysis, exploratory data analysis, outlier removal, non-parametric testing, and parametric hypothesis testing.

## Objectives

- Validate whether randomly sampled groups are statistically equivalent before experimentation.
- Calculate an appropriate sample size using statistical power analysis.
- Explore user behaviour through visualisation.
- Detect and remove outliers using the 99th percentile.
- Compare experimental and control groups using both non-parametric and parametric statistical tests.
- Determine whether the redesigned interface significantly affects Average Order Value (AOV).

## Project Structure

```
A-B-Test-for-Delivery-App/
│
├── data/
│   ├── aa_test.csv
│   └── ab_test.csv
│
├── src/
│   ├── 01_sampling_validation.py
│   ├── 02_sample_size_calculation.py
│   ├── 03_eda_and_outlier_removal.py
│   ├── 04_mann_whitney_test.py
│   └── 05_parametric_ab_test.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Analysis Workflow

### 1. Sampling Validation

- Levene's Test for equality of variances
- Independent two-sample t-test
- Verified that the initial sampling procedure produced statistically equivalent groups.

### 2. Sample Size Calculation

- Statistical power analysis
- Effect size = 0.2
- Power = 0.80
- Significance level = 0.05

Calculated the minimum sample size required for a reliable A/B experiment.

### 3. Exploratory Data Analysis

- Session count by day
- Order value distribution
- Session duration distribution
- Outlier detection using the 99th percentile
- Summary statistics after removing outliers

### 4. Non-Parametric A/B Test

Performed a Mann–Whitney U test to compare the distributions of the control and experimental groups without assuming normality.

### 5. Parametric A/B Test

- Applied a natural logarithm transformation to the order values
- Verified equal variances using Levene's Test
- Conducted an independent two-sample t-test on the transformed data

This provides an alternative statistical approach to validate the experimental results.

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Statsmodels
- Matplotlib

## Statistical Methods

- Levene's Test
- Independent Two-Sample t-test
- Mann–Whitney U Test
- Power Analysis
- Percentile-Based Outlier Detection
- Log Transformation

## Key Skills Demonstrated

- A/B Testing
- Statistical Hypothesis Testing
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Outlier Detection
- Data Visualisation
- Experimental Design
- Statistical Power Analysis
- Python Data Analysis

## Running the Project

1. Clone the repository.

```bash
git clone https://github.com/yourusername/A-B-Test-for-Delivery-App.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Execute any script inside the `src` directory.

For example:

```bash
python src/03_eda_and_outlier_removal.py
```

## Author

**Mankirat Kaur Dhillon**

Completed as part of my data analytics portfolio to demonstrate practical application of statistical testing, exploratory data analysis, and experimental design using Python.