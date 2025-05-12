import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print(x)
# (array([3, 5, 6],)

for i in x[0]:
    print(i)
    print("---")

# where the values are even:
x = np.where(arr % 2 == 0)
# values are odd:
x = np.where(arr % 2 == 0)
