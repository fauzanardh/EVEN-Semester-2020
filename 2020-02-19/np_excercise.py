import numpy as np


# Concatenate two 3x1 arrays of zeros and ones and get its shape.
def concatenate():
    first = np.zeros((3, 1))
    second = np.ones((3, 1))
    concatenated = np.concatenate((first, second))
    print(concatenated)


# Select the first column of a random 2x3 array.
def first_column():
    random_array = np.random.random((2, 3))
    selected = random_array[0]
    print(selected)


# Transpose a random 2x3 array into a 3x2 array
def transpose():
    random_array = np.random.random((2, 3))
    transposed = random_array.transpose()
    print(transposed)


# Reshape a random 2x3 array into a 3x2 array
def reshape():
    random_array = np.random.random((2, 3))
    reshaped = random_array.reshape((3, 2))
    print(reshaped)


# Create a random 2x3 and round it
def _round():
    random_array = np.random.random((2, 3))
    rounded = random_array.round()
    print(rounded)


# Create a 100x1 array of random sample from a normal (Gaussian) distribution
# and calculate its min max mean and standard deviation.
def do_something():
    random_normal_array = np.random.normal(size=(100, 1))
    _min = np.amin(random_normal_array)
    _max = np.amax(random_normal_array)
    _mean = np.mean(random_normal_array)
    _std = np.std(random_normal_array)
    print(_min, _max, _mean, _std)


# Calculate the element-wise multiplication of two random arrays of size 3x3
def multiply():
    random_array = np.random.random((3, 3))
    random_array_2 = np.random.random((3, 3))
    multiplied = np.multiply(random_array, random_array_2)
    print(multiplied)


# Calculate the matrix multiplication of two random arrays of size 2x3 and 3x4
def multiply2():
    random_array = np.random.random((2, 3))
    random_array_2 = np.random.random((3, 4))
    multiplied = np.dot(random_array, random_array_2)
    print(multiplied)


# Check that infinity is greater than 1000
def check_infinity():
    inf = np.Infinity
    if inf > 1000:
        print("Infinity is greater than 1000")
    else:
        print("1000 is greater than Infinity")


# Assignment
# Given two dimension arrays, extract unique rows from both arrays
def unique():
    array = np.array([1, 2, 3], [4, 5, 6])
    array_2 = np.array([1, 2, 3], [6, 7, 8])
    concat = np.concatenate((array, array_2))
    _unique = np.unique(concat)
    print(_unique)
