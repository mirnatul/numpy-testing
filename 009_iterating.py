# we can use basic for loop of python
# nd dimension will have n loop to get single item

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    # print(x)
    pass


arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        # print(y)
        pass


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)
    print("---")
