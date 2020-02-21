import scipy as sp
import pandas as pd
from scipy import stats

# Read csv data from
df = pd.read_csv("dataset/salaries.csv")

# Give the summary for the numeric columns in the dataset
cols = []
_sum = df.loc[:, ["phd", "service", "salary"]].sum()
print("\nSUM")
print(_sum)

# Calculate standard deviation for all numeric columns;
_std = df.loc[:, ["phd", "service", "salary"]].std()
print("\nSTD")
print(_std)

# Mean values of the first 50 records
_mean = df.iloc[:50].mean()
print("\nMEAN")
print(_mean)
