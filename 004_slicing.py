# [start:end] or [start:end:step] (end not include)
# if don't start consider as 0, if don't end consider as last
# [:5] or [1:]] or [-3:-1] or [1:5:2] or [::2]

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])


# 2-D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])  # [7, 8, 9]
# from 0 and 1 return 2
print(arr[0:2, 2])  # [3, 8]
# from 0 and 1 return 1, 2, 3
print(arr[0:2, 1:4])  # [[2, 3, 4] [7, 8, 9]]
