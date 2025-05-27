import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
# [15-10, 25-15, 5-25] = [5 10 -20]
# here n = 1, if n = 2 it will do it again

newarr = np.diff(arr, n=2)  # [5 -30]

print(newarr)
