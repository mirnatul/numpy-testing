import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

# sum of all two array
newarr = np.sum([arr1, arr2])  # 12

# to sum all arrays item separately
newarr = np.sum([arr1, arr2], axis=1)  # [6 6]

# commulative sum (for an item all all previous)
newarr = np.cumsum(arr1)  # [1 3 6]

print(newarr)
