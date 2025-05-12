print("Hello, NumPy")


import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.concatenate((a, b), axis=0)

# print(result)


a = np.array([1, 2])
b = np.array([3, 4])
result = np.stack((a, b), axis=1)
# Output: [[1 2], [3 4]]
# print(result)


test = np.array([[[1, 5], [2, 6]], [[3, 7], [4, 8]]])
test2 = np.array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])

res = np.concatenate((test, test2), axis=0)
print(res)
