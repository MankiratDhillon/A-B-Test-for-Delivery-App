import numpy as np
from pathlib import Path
import pandas as pd
from scipy.stats import mannwhitneyu

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Read the dataset
data = pd.read_csv(DATA_DIR / "ab_test.csv")

# Calculate the 99th-percentile limits using the whole dataset
order_limit = np.percentile(data["order_value"], 99)
duration_limit = np.percentile(data["session_duration"], 99)

# Remove rows that are outliers in either variable
filtered = data[
    (data["order_value"] <= order_limit)
    & (data["session_duration"] <= duration_limit)
]

# Separate order values for the two groups
control = filtered.loc[
    filtered["group"] == "Control",
    "order_value"
]

experimental = filtered.loc[
    filtered["group"] == "Experimental",
    "order_value"
]

# Perform a two-sided Mann-Whitney U test
u1, p_value = mannwhitneyu(
    control,
    experimental,
    alternative="two-sided"
)

reject_null = p_value <= 0.05

print("Mann-Whitney U test")
print(
    f"U1 = {u1:.1f}, "
    f"p-value {'<= 0.05' if reject_null else '> 0.05'}"
)
print(f"Reject null hypothesis: {'yes' if reject_null else 'no'}")
print(f"Distributions are same: {'no' if reject_null else 'yes'}")