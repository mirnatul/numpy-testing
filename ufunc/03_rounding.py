import numpy as np

arr = np.trunc([-3.1666, 3.6667])
arr1 = np.fix([-3.1666, 3.6667])
# output: [-3.  3.] -> which is floating number

# print(arr, arr1)

arr = np.around(3.1666, 2)  # 3.17
# print(arr)

arr = np.floor([-3.1666, 3.6667])  # [-4. 3.]
# print(arr)

arr = np.ceil([-3.1666, 3.6667])  # [-3. 4.]
print(arr)
