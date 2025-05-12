import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

# print(x)

arr = np.array([5, 6, 7, 7, 8, 9, 10])
x = np.searchsorted(arr, 7, side="left")  # left is by default
y = np.searchsorted(arr, 7, side="right")
print(x, y)  # 2 4


arr2 = np.array([1, 3, 5, 7])
z = np.searchsorted(arr2, [2, 4, 6])
print(z)  # [1, 2, 3]
