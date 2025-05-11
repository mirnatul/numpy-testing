# iterating arrays using nditer()
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)


# iterating array with different data types
# buffered allows changing the data type during iteration safely
arr1 = np.array([1, 2, 3])
for x in np.nditer(arr1, flags=["buffered"], op_dtypes=["float"]):
    print(x)

# iterate with different step size
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr2[:, ::2]):  # all row the 2 step of each row
    print(x)

# enumerate(): mentioning sequence number of somethings one by one
arr3 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr3):
    print(idx, x)  # tuple of index and value Ex, (0,) 1

arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr4):
    print(idx, x)

# (0, 0) 1
# (0, 1) 2 etc
