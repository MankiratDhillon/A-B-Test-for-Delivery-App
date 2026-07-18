import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Read the dataset
data = pd.read_csv(DATA_DIR / "ab_test.csv")

# Convert the date column to datetime and extract the day
data["date"] = pd.to_datetime(data["date"])
data["day"] = data["date"].dt.day

# Plot number of sessions by day for each group
sessions = (
    data.groupby(["day", "group"])
    .size()
    .unstack()
)

sessions.plot(kind="bar")
plt.xlabel("April")
plt.ylabel("Number of sessions")
plt.show()

# Plot order value histograms
data.hist(column="order_value", by="group")
plt.xlabel("Order value")
plt.show()

# Plot session duration histograms
data.hist(column="session_duration", by="group")
plt.xlabel("Session duration")
plt.show()

# Calculate the 99th percentiles
order_limit = np.percentile(data["order_value"], 99)
duration_limit = np.percentile(data["session_duration"], 99)

# Remove outliers
filtered = data[
    (data["order_value"] <= order_limit)
    & (data["session_duration"] <= duration_limit)
]

# Print statistics
print(f"Mean: {filtered['order_value'].mean():.2f}")
print(f"Standard deviation: {filtered['order_value'].std(ddof=0):.2f}")
print(f"Max: {filtered['order_value'].max():.2f}")