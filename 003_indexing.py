import numpy as np


# accessing array
arr = np.array([1, 2, 3, 4])
print(arr[2])

# accessing 2-D array
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element in the 1st row: ", arr_2d[0, 1])  # 2
print("Last element from 2nd dim: ", arr_2d[1, -1])  # 10

# access 3-D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d[0, 1, 2])  # 6
