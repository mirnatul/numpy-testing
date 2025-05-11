import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 42
x[3] = 27

print(arr)
print(x)


# check if array owns its data

print(x.base)  # None - copy
print(y.base)  # [1, 2, 3, 4, 5] - view
