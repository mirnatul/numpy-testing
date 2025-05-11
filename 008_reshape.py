import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 1d to 2d
arr_2d = arr.reshape(4, 3)
print(arr_2d)  # [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# 1d to 3d
arr_3d = arr.reshape(2, 3, 2)
print(arr_3d)  # [[[1,2],[3,4],[5,6]], [[7,8],[9,10],[11,12]]]

# we can't reshape to any shape the multiplication should be the length of the array
# example 2*3*2 = 12 (which is array length)

# reshape return a view or copy,
# if the new shape is compatible with the original array's memory layout, and the array is C-contiguous (stored in row-major order), then reshape() returns a view otherwise it returns a copy

# unknown dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)  # auto detect to 2 (2*2*2=8)


# flattening the array (multi dimension to 1 dimension) (-1)
arr_multi = np.array([[1, 2, 3], [4, 5, 6]])
arr_one = arr.reshape(-1)
print(arr_one)
