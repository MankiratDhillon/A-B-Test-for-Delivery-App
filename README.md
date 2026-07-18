# A/B Test for Delivery App

A Python data analysis project investigating whether a redesigned food delivery application interface affects **Average Order Value (AOV)** using statistical hypothesis testing.

This project was completed as part of the **HyperSkill Academy Data Analyst learning track** and demonstrates an end-to-end A/B testing workflow using Python, pandas, NumPy, SciPy, Statsmodels, and Matplotlib.

## Project Overview

A/B testing is used to compare two versions of a product, service, or interface and determine whether an observed difference is likely to represent a genuine effect rather than random variation.

In this project:

* the control group represents users of the original application interface
* the experimental group represents users of the redesigned interface
* Average Order Value is used as the primary outcome being evaluated

The project begins by assessing whether the initial samples are statistically comparable. It then calculates an appropriate experiment size, explores the collected data, handles extreme values, and compares the control and experimental groups using both non-parametric and parametric statistical methods.

## Project Objectives

* Assess whether randomly selected groups are statistically comparable.
* Calculate an appropriate sample size using statistical power analysis.
* Explore user sessions and order-value distributions.
* Identify and remove extreme values using the 99th percentile.
* Compare control and experimental groups without assuming normality.
* Apply a transformation and conduct a parametric comparison.
* Interpret statistical test results using a defined significance level.
* Organise the experiment into a clear and reproducible Python repository.

## Project Structure

```text
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

Before interpreting an A/B experiment, the project assesses whether the initial groups were created through an appropriate random sampling process.

The validation stage uses:

* Levene’s test to compare group variances
* an independent two-sample t-test to compare group means
* p-value interpretation using the selected significance level

This stage helps determine whether any initial differences between the samples are likely to be caused by random variation.

### 2. Sample Size Calculation

Statistical power analysis is used to calculate the minimum sample size required for the experiment.

The calculation uses:

* effect size: `0.2`
* statistical power: `0.80`
* significance level: `0.05`

Selecting an appropriate sample size helps reduce the risk of conducting an experiment that is too small to reliably detect a meaningful effect.

### 3. Exploratory Data Analysis

The exploratory analysis examines the structure and behaviour of the experiment data before hypothesis testing.

The stage includes:

* converting the date column to a datetime format
* extracting the day from each observation
* comparing session counts by day and group
* visualising order-value distributions
* visualising session-duration distributions
* calculating descriptive statistics
* identifying extreme order values
* removing observations above the 99th percentile
* reviewing the data after outlier removal

This stage helps identify skewness, unusual observations, and distributional differences that may influence the selection of statistical methods.

### 4. Non-Parametric A/B Test

A Mann–Whitney U test is used to compare the order-value distributions of the control and experimental groups.

This test is appropriate when:

* the data may not be normally distributed
* the observations are independent
* the analysis requires a comparison that does not rely on a normality assumption

The result is interpreted using the calculated p-value and the selected significance threshold.

### 5. Parametric A/B Test

A second analysis is performed using a parametric approach.

The stage includes:

* applying a natural logarithm transformation to order values
* using Levene’s test to assess the equality of variances
* conducting an independent two-sample t-test on the transformed data
* interpreting the resulting test statistic and p-value

The transformation reduces the influence of skewness and allows the experimental conclusion to be examined using an alternative statistical method.

## Technologies Used

* Python
* pandas
* NumPy
* SciPy
* Statsmodels
* Matplotlib

## Statistical Methods

* Levene’s test for equality of variances
* independent two-sample t-test
* Mann–Whitney U test
* statistical power analysis
* percentile-based outlier detection
* natural logarithm transformation
* descriptive statistical analysis
* p-value and significance-level interpretation

## Skills Demonstrated

### Experimental Design

* understanding control and experimental groups
* validating random sampling
* selecting a measurable experiment outcome
* defining a significance level
* calculating a required sample size
* considering statistical power and effect size

### Data Preparation and Analysis

* loading CSV data with pandas
* converting dates to datetime values
* extracting date components
* filtering observations
* splitting data by experimental group
* calculating percentiles
* removing extreme values
* calculating descriptive statistics
* transforming skewed numerical data

### Statistical Testing

* testing equality of variances
* conducting independent t-tests
* conducting Mann–Whitney U tests
* selecting parametric and non-parametric methods
* interpreting test statistics
* interpreting p-values
* evaluating evidence against a null hypothesis

### Data Visualisation

* comparing session counts by day
* producing grouped bar charts
* producing order-value histograms
* producing session-duration histograms
* visually examining skewness and extreme values
* comparing control and experimental distributions

### Software and Project Practices

* separating an analysis into logical stages
* using relative file paths
* managing Python dependencies
* documenting assumptions and methods
* maintaining a reproducible GitHub repository
* presenting technical work through structured documentation

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/A-B-Test-for-Delivery-App.git
cd A-B-Test-for-Delivery-App
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Activate the environment on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the scripts from the repository root in numerical order:

```bash
python src/01_sampling_validation.py
python src/02_sample_size_calculation.py
python src/03_eda_and_outlier_removal.py
python src/04_mann_whitney_test.py
python src/05_parametric_ab_test.py
```

Individual stages can also be executed separately. For example:

```bash
python src/03_eda_and_outlier_removal.py
```

Scripts containing visualisations will open the relevant charts in separate windows.

## Dataset Note

The datasets used in this project were supplied as part of the HyperSkill Academy project materials.

They are included for educational and portfolio purposes.

## Author

**Mankirat Kaur Dhillon**

Completed as part of a data analytics portfolio demonstrating practical A/B testing, statistical analysis, exploratory data analysis, and experimental design using Python.
