# create an array using choice and size also set probability
# p's total must be 1

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))
# [7 7 3 7 7 5 5 7 7 5] or [7 7 7 5 7 7 5 7 7 7] or etc...
# print(x)

y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(y)
