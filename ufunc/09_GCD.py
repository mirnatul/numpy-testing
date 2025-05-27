import numpy as np

num1, num2 = 6, 9
x = np.gcd(num1, num2)  # 3

# find gcd from array
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)  # 4

print(x)
