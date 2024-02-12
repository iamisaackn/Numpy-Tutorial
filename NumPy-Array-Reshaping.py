# Reshaping arrays
''' 
By reshaping we can add or remove dimensions or change number of elements in each dimension.
'''

# ------------------------------- Reshape From 1-D to 2-D ---------------------
import numpy as np # import Numpy library

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x = arr.reshape(4, 3) # 4 arrays, each with 3 elements
print(x) # [[ 1  2  3][ 4  5  6][ 7  8  9][10 11 12]]

# ---------------------------- Reshape From 1-D to 3-D -------------------------
import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x = arr.reshape(2, 3, 2) #  2 arrays that contains 3 arrays, each with 2 elements
print(x) # [[[ 1  2] [ 3  4] [ 5  6]] [[ 7  8] [ 9 10] [11 12]]]

# ---------------------------- Returns Copy or View? -------------
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base) # VIEW "[1 2 3 4 5 6 7 8]"


# ---------------------------- Flattening the arrays -------------------
'''
Flattening array means converting a multidimensional array into a 1D array.
We can use reshape(-1) to do this.
'''
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

x = arr.reshape(-1)
print(x) # [1 2 3 4 5 6 7 8]