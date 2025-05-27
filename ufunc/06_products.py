import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)  # multi of all item 24

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])  # 40320

# product over axis
x = np.prod([arr1, arr2], axis=1)  # [24 1680]

# commulative product
x = np.cumprod(arr)  # [1 2 6 24]

print(x)
