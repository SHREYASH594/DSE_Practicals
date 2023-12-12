import pandas as pd

# a. Create and sort a series by index and values
series_a = pd.Series([40, 10, 30, 20, 50], index=['d', 'a', 'c', 'b', 'e'])
print("Original Series:\n", series_a)
sorted_by_index = series_a.sort_index()
sorted_by_values = series_a.sort_values()
print("Sorted by index:\n", sorted_by_index)
print("Sorted by values:\n", sorted_by_values)

# b. Find minimum and maximum ranks using 'first' and 'max' methods
N = 10  # Number of elements in the series
series_b = pd.Series([1, 3, 5, 3, 2, 5, 1, 4, 4, 2])  # Replace with your elements
rank_first = series_b.rank(method='first')  # Assigns ranks in the order they appear
rank_max = series_b.rank(method='max')  # Assigns maximum rank to duplicated values
print("Original Series:\n", series_b)
print("Ranks with 'first' method:\n", rank_first)
print("Ranks with 'max' method:\n", rank_max)

# c. Display index value of minimum and maximum elements
min_index = series_b.idxmin()
max_index = series_b.idxmax()
print("Index of minimum element:", min_index)
print("Index of maximum element:", max_index)
