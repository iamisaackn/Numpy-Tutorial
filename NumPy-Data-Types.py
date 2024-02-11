'''
List of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

'''
# Import necessary library
import numpy as np

# ----------- Checking the Data Type of an Array ----------------

# Use the NumPy array object property "dtype"
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'orange'])
print(arr.dtype)

# ---------- Creating Arrays With a Defined Data Type -----------------

# We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements.
arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well.
arr = np.array([1, 2, 3, 4], dtype= 'i4') # 4 byte integer
print(arr)
print(arr.dtype)

# --------------- Converting Data Type on Existing Arrays ----------------

# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
#  you can use the data type directly like float for float and int for integer.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
new1 = arr.astype('S4')
new2 = arr. astype('float')
new3 = arr. astype('int')

print(new1)
print(new1.dtype)

print(new2)
print(new2.dtype)

print(new3)
print(new3.dtype)