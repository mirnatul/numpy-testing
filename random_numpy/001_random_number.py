# generate random number

from numpy import random

x = random.randint(100)

print(x)

# generate random float
y = random.rand()
print(y)

# generate random array
arr = random.randint(100, size=(5))

print(arr)

# generate 2D array (row, column)
arr_2D = random.randint(100, size=(3, 5))
print(arr_2D)

# float array
float_1D = random.rand(5)
print(float_1D)

# float 2D array
float_2D = random.rand(3, 5)
print(float_2D)


# generate random number form array
rand_from_arr = random.choice([3, 5, 7, 9])
print(rand_from_arr)

# the choice method also allow us to create array with given number
cr_arr = random.choice([3, 5, 7, 9], size=(3, 5))
print(cr_arr)
