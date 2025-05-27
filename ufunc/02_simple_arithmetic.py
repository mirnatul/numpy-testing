# any array like object e.g. lists, tuples etc
import numpy as np

# addition
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

add_arr = np.add(arr1, arr2)
subtract_arr = np.subtract(arr1, arr2)
multiply_arr = np.multiply(arr1, arr2)
divide_arr = np.divide(arr1, arr2)
power_arr = np.power(arr1, arr2)
# mod and remainder both are same
mod_arr = np.mod(arr1, arr2)
remainder_arr = np.remainder(arr1, arr2)
# give both quotient and the mod
# (array([0, 0, 0, 0, 0, 0]), array([10, 11, 12, 13, 14, 15]))
divmod_arr = np.divmod(arr1, arr2)
# absolute value
absolute_arr = np.absolute(arr1)


print(absolute_arr)
