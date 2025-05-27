import numpy as np


arr = np.arange(1, 10)

print(np.log2(arr))  # base 2
print(np.log10(arr))  # base 10
print(np.log(arr))  # base e

# custom log
from math import log

nplog = np.frompyfunc(log, 2, 1)
# 2 is the number of input and 1 is the number of output

print(nplog(100, 15))
