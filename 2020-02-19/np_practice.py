import numpy as np

# 1D numpy array
A = np.array([1, 2, 3, 4])

# 2D numpy array
B = np.array([[1, 2, 3], [4, 5, 6]])
# 2D zero-fill numpy array
C = np.zeros((2, 3))
# 2D one-fill numpy array
D = np.ones((2, 3))
# 2D diagonal numpy array
E = np.diag([1, 2])

# Generating numpy arrays
F = np.arange(0, 6, 2)
G = np.linspace(0, 1, 5)

# Numpy functions
arr = np.ones((2, 3))
# Reshaping the array
reshaped = arr.reshape((3, 2))
# Flattening the array
flatten = arr.flatten()
