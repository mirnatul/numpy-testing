import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1.dtype)

arr2 = np.array(["apple", "banana", "cherry"])
print(arr2.dtype)


arr3 = np.array([1, 2, 3, 4], dtype="S")  # |S1
print(arr3, arr3.dtype)

# 4 byte integer
arr4 = np.array([1, 2, 3, 4], dtype="i4")  # int32


# wrong conversion will give an error
arr5 = np.array(["a", "2", "3"], dtype="i")  # raise ValueError

# converting data type on existing array, copy of the array, and allow to specify the data type
arr = np.array([1.1, 2.1, 3.1])
# "i" is int32 type and int is int64 type and bool will convert True or False
newarr = arr.astype("i")
print(newarr)
