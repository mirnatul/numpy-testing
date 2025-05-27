import numpy as np

num1, num2 = 4, 8
x = np.lcm(num1, num2)  # 8

# find lcm in array
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)  # 18

print(x)
