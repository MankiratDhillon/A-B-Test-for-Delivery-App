import math
from pathlib import Path
import pandas as pd
from statsmodels.stats.power import tt_ind_solve_power

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Calculate sample size
sample_size = tt_ind_solve_power(
    effect_size=0.2,
    power=0.8,
    alpha=0.05,
    ratio=1
)

# Round up to the next hundred
sample_size = math.ceil(sample_size / 100) * 100

# Read dataset
data = pd.read_csv(DATA_DIR / "ab_test.csv")

# Count groups
group_counts = data["group"].value_counts()

control_count = group_counts["Control"]
experimental_count = group_counts["Experimental"]

print(f"Sample size: {sample_size}")
print()
print(f"Control group: {control_count}")
print(f"Experimental group: {experimental_count}")