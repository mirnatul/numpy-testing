import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)  # [1 2 3 4 5 6 7]

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

# finding union
x = np.union1d(arr1, arr2)  # [1 2 3 4 5 6]

# finding intersection
x = np.intersect1d(arr1, arr2, assume_unique=True)  # [3 4]
# assume_unique is set to True can speed up computation

# finding difference
x = np.setdiff1d(arr1, arr2, assume_unique=True)  # [1 2]

# finding symmetric difference
x = np.setxor1d(arr1, arr2, assume_unique=True)  # [1 2 5 6]

print(x)
