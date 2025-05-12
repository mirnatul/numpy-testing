# more array to a single array
# in numpy we join arrays by axes

# if axis is not explicitly passed, it is taken as 0

# concatenate: join a sequence of arrays along an existing axis

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2), axis=0)
# axis=0: [1,2,3,4,5,6]
# print(arr)


arr1_2 = np.array([[1, 2], [3, 4]])
arr2_2 = np.array([[5, 6], [7, 8]])

arr_2 = np.concatenate((arr1_2, arr2_2), axis=0)
# axis=0: [[1,2],[3,4],[5,6],[6,7]]
# axis=1: [[1,2,5,6],[3,4,7,8]]
# print(arr_2)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
# axis=0: [[1,2,3],[4,5,6]]
# axis=1: [[1,4],[2,5],[3,6]]
# print(arr)


arr1_2 = np.array([[1, 2], [3, 4]])
arr2_2 = np.array([[5, 6], [7, 8]])

arr_2 = np.stack((arr1_2, arr2_2), axis=2)
# axis=0: [[[1,2],[3,4]],[[5,6],[7,8]]]
# axis=1: [[[1,2],[5,6]],[[3,4],[7,8]]]
# axis=2: [[[1,5],[2,6]],[[3,7],[4,8]]]
print(arr_2)
