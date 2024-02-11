# Importing necessary libraries
import numpy as np

# ---------------- Access Array Elements ----------------
# You can access an array element by referring to its index number.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3]) # ADDITION

# ---------------- Access 2-D Arrays --------------------------
# Use comma separated integers representing the dimension and the index of the element.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2nd element in the 1st row: ", arr[0, 1])
print("2nd element in the 2nd row: ", arr[1, 1])
print("2nd element from both rows: ", arr[0, 1], ",",arr[1, 1])

# ------------- Access 3-D Arrays ----------------
# Use comma separated integers representing the dimensions and the index of the element.
arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 12, 13]]])
print(arr[0, 1, 2])
print(arr[1, 0, 2])
print(arr[0, 0, 2] + arr[1, 1, 2])

# ------------- Negative Indexing ---------------------
# Used to access an array from the end.
arr = np.array([[[1, 2, 13], [3, 4, 15]], [[5, 6, 7], [8, 9, 10]]])
print("Output last element: ", arr[1, 1, -1])
print(arr[0, 0, -2])
print(arr[0, 1, -2] * arr[1, 1, -3])