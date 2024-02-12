# Shape of an Array
'''
The shape of an array is the number of elements in each dimension.
'''

# ------------------ Get the Shape of an Array ---------
'''
NumPy arrays have an attribute called 'shape' that returns a tuple with each index having the number of corresponding elements.
'''
import numpy as np # Import Numpy library

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4]])

print(arr1.shape) # (3, 4)
print(arr.shape) # (2, 4) The array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

# Create an array with 5 dimensions using 'ndmin' using a vector with values 1,2,3,4 and verify that last dimension has value 4:
import numpy as np # Importing Numpy Library

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr.shape) # (1, 1, 1, 1, 4)

