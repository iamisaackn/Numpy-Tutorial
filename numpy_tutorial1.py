# Importing necessary libraries
import numpy as np
import time
import sys

# ----------------- DIFF in SIZE ---------------------------

# Creating a list and a numpy array of numbers from 0 to 999
l = range(1000)
array = np.arange(1000)

# Printing the total memory occupied by the list and the numpy array
print(sys.getsizeof(5)*len(l))  # Memory used by Python list
print(array.size*array.itemsize)  # Memory used by Numpy array

# -------------------- DIFF in SPEED ---------------------

# Creating two lists and two numpy arrays of size 1,000,000
SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Calculating the time taken to add two lists and two numpy arrays
start = time.time()
result = [(x + y) for x,y in zip (l1, l2)]  # Adding two Python lists
print("Time taken by Python List: ", (time.time() - start) * 1000)

start = time.time()
result = a1 + a2  # Adding two Numpy arrays
print("Tme taken by Numpy Array: ", (time.time() - start) * 1000)


