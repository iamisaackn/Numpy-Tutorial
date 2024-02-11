# Import necessary libraries
import numpy as np

# -------------------- Slicing arrays -------------

# It means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5]) # [START:END]
print(arr[ : 5]) # [ : END]
print(arr[1: ]) # [START : ]

# ----------------------- Negative Slicing -----------------------

# Use the minus operator to refer to an index from the end.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[-6:-1])
print(arr[ :-4])
print(arr[-4: ])

# --------------------------- STEP ---------------------------------

# Use the step value to determine the step of the slicing.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[0: 5: 3])
print(arr[ ::3])
print(arr[0::2])
print(arr[ :5:2])


# ------------------------- Slicing 2-D Arrays -----------------------

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 0:2])
print(arr[0, 0:2])
print(arr[0:2, 2]) # Reterns index 2 
print(arr[0:3, 1:3])

