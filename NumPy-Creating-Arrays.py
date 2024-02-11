# Import necessary libraries
import numpy as np

# -------- Create a NumPy ndarray Object ----------

# Usiny the array() function to create Numpy ndarray
arr = np.array([1, 2, 3, 4, 5])

# Printing the array and type
print(arr)
print(type(arr)) # type() tells the type of object passed to it.


# -------------- Dimensions in Array ----------------

# A dimension in arrays is one level of array depth (nested arrays).
# nested array: are arrays that have arrays as their elements.

                # 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
a = np.array(422)
print(a)

                 # 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b)

                 # 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(c)

                # 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print (d)

# ---------------- Check Number of Dimensions? -----------------
# Use ndim attribute

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# ----------------- Higher Dimensional Arrays ---------
# When the array is created, you can define the number of dimensions by using the ndmin argument.

e = np.array([1, 2, 3, 4, 5], ndmin = 5)
print(e)
print('Number of dimension: ', e.ndim)