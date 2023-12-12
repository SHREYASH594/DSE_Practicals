import numpy as np

# a. Create ARR1 with random values from 0 to 1, compute mean, std, and variance along the second axis
ARR1 = np.random.rand(3, 4)  # Example shape (3, 4), change dimensions as needed
print("ARR1:\n", ARR1)
mean_arr1 = np.mean(ARR1, axis=1)
std_arr1 = np.std(ARR1, axis=1)
var_arr1 = np.var(ARR1, axis=1)
print("Mean along axis 1:", mean_arr1)
print("Standard deviation along axis 1:", std_arr1)
print("Variance along axis 1:", var_arr1)

# b. Create and reshape array based on user inputs
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
arr2d = np.random.randint(0, 10, size=(m, n))  # Random integer array of size m x n
print("Array 2D shape:", arr2d.shape)
print("Array 2D type:", type(arr2d))
print("Array 2D data type:", arr2d.dtype)
reshaped_arr = np.reshape(arr2d, (n, m))
print("Reshaped array:\n", reshaped_arr)

# c. Test for zero, non-zero, NaN elements in a given 1D array
arr_1d = np.array([0, 3, 5, 0, np.nan, 8, 0])
zero_indices = np.where(arr_1d == 0)[0]
nonzero_indices = np.where(arr_1d != 0)[0]
nan_indices = np.where(np.isnan(arr_1d))[0]
print("Indices of zeros:", zero_indices)
print("Indices of non-zeros:", nonzero_indices)
print("Indices of NaNs:", nan_indices)

# d. Operations on arrays
Array1 = np.random.rand(3, 3)
Array2 = np.random.rand(3, 3)
Array3 = np.random.rand(3, 3)
Array4 = Array3 - Array2
Array5 = Array1 * 2
covariance = np.cov(Array1.flatten(), Array4.flatten())
correlation = np.corrcoef(Array1.flatten(), Array5.flatten())
print("Covariance between Array1 and Array4:\n", covariance)
print("Correlation between Array1 and Array5:\n", correlation)

# e. Operations on random arrays
Array1 = np.random.rand(10)
Array2 = np.random.rand(10)
sum_first_half = np.sum(Array1[:5]) + np.sum(Array2[:5])
product_second_half = np.prod(Array1[5:]) * np.prod(Array2[5:])
print("Sum of first half of both arrays:", sum_first_half)
print("Product of second half of both arrays:", product_second_half)

# f. Determine memory occupied by an array
random_array = np.random.rand(5, 5)
memory_size = random_array.nbytes
print("Memory occupied by the array:", memory_size, "bytes")

# g. Operations on a 2D array
m, n = 4, 3  # Example size m x n, change as needed
arr_2d = np.random.randint(10, 100, size=(m, n))
print("Original Array:\n", arr_2d)
# Swap rows 1 and 2
arr_swapped_rows = arr_2d.copy()
arr_swapped_rows[[1, 2]] = arr_swapped_rows[[2, 1]]
print("Array with swapped rows:\n", arr_swapped_rows)
# Reverse a specified column (column 1 in this case)
specified_column = 1
arr_reversed_col = arr_2d.copy()
arr_reversed_col[:, specified_column] = arr_reversed_col[::-1, specified_column]
print("Array with reversed column:\n", arr_reversed_col)
