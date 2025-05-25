from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# permutation return a shuffled array (don't change original)
re_arr = random.permutation(arr)

# make changes of the original array
random.shuffle(arr)

print(re_arr)
print(arr)
