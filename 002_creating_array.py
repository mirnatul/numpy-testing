import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# we can pass a list, tuple or any array-like object
arr = np.array((1, 2, 3, 4, 5))

# Dimensions

# 0-D array
arr_0d = np.array(27)
# print(arr_0d)

# 1-D array
arr_1d = np.array([1, 2, 3])
# print(arr_1d)

# 2-D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2d)

# 3-D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr_3d)
# print(arr_3d.ndim)  # 3

# higher dimensional array
arr_higher = np.array([1, 2, 3, 4], ndmin=5)

print(arr_higher)
print(arr_higher.ndim)
