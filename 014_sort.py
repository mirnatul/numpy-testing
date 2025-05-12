import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
# this returns a copy of the array, leaving the original array unchanged

# sort by alphabetic (case-sensitive)
arr = np.array(["banana", "cherry", "apple"])
print(np.sort(arr))  # A-Z then a-z

# sort by boolean
arr = np.array([True, False, True])
print(np.sort(arr))  # False then True

# sort 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))  # [[2, 3, 4], [0, 1, 5]]
