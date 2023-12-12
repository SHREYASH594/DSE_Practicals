import pandas as pd
import numpy as np

# Creating a DataFrame with 3 columns and 50 rows of random numeric data
np.random.seed(42)
data = {
    'A': np.random.rand(50),
    'B': np.random.rand(50),
    'C': np.random.rand(50)
}
df = pd.DataFrame(data)

# Replacing 10% of values with NaN at random positions
rows, cols = df.shape
null_indices = [(np.random.randint(0, rows), np.random.randint(0, cols)) for _ in range(int(0.1 * rows * cols))]
for i, j in null_indices:
    df.iloc[i, j] = np.nan

# a. Identify and count missing values in the DataFrame
missing_values_count = df.isnull().sum()
print("Missing values count:\n", missing_values_count)

# b. Drop column having more than 5 null values
df = df.dropna(thresh=df.shape[0]-5, axis=1)
print("DataFrame after dropping columns:\n", df)

# c. Identify row label having maximum sum of all values in a row and drop that row
max_sum_row_label = df.sum(axis=1).idxmax()
df = df.drop(max_sum_row_label)
print("DataFrame after dropping row with maximum sum:\n", df)

# d. Sort DataFrame based on the first column
df = df.sort_values(by='A')
print("DataFrame sorted on the basis of first column:\n", df)

# e. Remove duplicates from the first column
df = df[~df['A'].duplicated()]
print("DataFrame after removing duplicates from first column:\n", df)

# f. Find correlation between first and second column, and covariance between second and third column
correlation = df['A'].corr(df['B'])
covariance = df['B'].cov(df['C'])
print("Correlation between first and second column:", correlation)
print("Covariance between second and third column:", covariance)

# g. Discretize the second column into 5 bins
df['B_discretized'] = pd.cut(df['B'], bins=5)
print("DataFrame with second column discretized into 5 bins:\n", df)
