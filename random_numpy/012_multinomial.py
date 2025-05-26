from numpy import random

x = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])

print(x)
# [1 2 0 3 0 0]
"""
face 1 - 1 times
face 2 - 2 times
face 3 - 0 times
face 4 - 3 times
face 5 - 0 times
face 6 - 0 times
"""
