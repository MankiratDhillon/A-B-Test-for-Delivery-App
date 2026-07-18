from pathlib import Path
import pandas as pd
from scipy.stats import levene, ttest_ind

# Get the project root and data folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Read the data
data = pd.read_csv(DATA_DIR / "aa_test.csv")

sample_1 = data["Sample 1"]
sample_2 = data["Sample 2"]

# Levene's test
w, p = levene(sample_1, sample_2)

equal_var = p > 0.05

print("Levene's test")
print(f"W = {w:.3f}, p-value {'> 0.05' if p > 0.05 else '<= 0.05'}")
print(f"Reject null hypothesis: {'no' if p > 0.05 else 'yes'}")
print(f"Variances are equal: {'yes' if equal_var else 'no'}")

print()

# Independent t-test
t, p = ttest_ind(sample_1, sample_2, equal_var=equal_var)

print("T-test")
print(f"t = {t:.3f}, p-value {'> 0.05' if p > 0.05 else '<= 0.05'}")
print(f"Reject null hypothesis: {'no' if p > 0.05 else 'yes'}")
print(f"Means are equal: {'yes' if p > 0.05 else 'no'}")


