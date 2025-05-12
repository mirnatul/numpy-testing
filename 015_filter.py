import numpy as np

arr = np.array([41, 42, 43, 44])


filter_arr = arr > 42  # here we place the condition
new_array = arr[filter_arr]
print(filter_arr)  # [False, False, True, True]
print(new_array)  # [43, 44]
