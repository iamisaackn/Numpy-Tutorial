# The Difference Between Copy and View
'''
1. The copy is a new array, and the view is just a view of the original array.
2. The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
3. The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''

# ----------------- COPY -----------------------------
# Make a copy, change the original array, and display both arrays:
import numpy as np # Importing necessary libraries

arr = np.array([1, 2, 3, 4, 5, 6, 7])
x = arr.copy() # Copying the original array
arr[0] = 42

print(arr) # Original "[42  2  3  4  5  6  7]"
print(x) # COPY "[1 2 3 4 5 6 7]"

# ------------------ VIEW ---------------------------
# Make a view, change the original array, and display both arrays:
import numpy as np # Importing necessary libraries

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view() # VIEW
arr[0] = 42

print(arr) # ORIGINAL "[42  2  3  4  5  6]"
print(x) # VIEW "[42  2  3  4  5  6]"

# Make Changes in the VIEW:
import numpy as np # Importing Numpy library

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view()
x[2] = 19 # Made changes to the view property

print(x) # [ 1  2 19  4  5  6]
print(x[2] * x[4]) # 95

# ------------------- Check if Array Owns its Data ------------------------
'''
Every NumPy array has the attribute 'base' that returns 'None' if the array owns the data.
Otherwise, the base  attribute refers to the original object. 
'''
import numpy as np # Importing Numpy library

arr = np.array([1, 2, 3, 4, 5, 6])

x = arr.copy() # COPY
y = arr.view() # VIEW

# Check if it owns the data
print(x.base) # None
print(y.base) # [1 2 3 4 5 6]