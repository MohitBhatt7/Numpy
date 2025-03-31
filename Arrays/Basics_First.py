import numpy as np
# Creating one dimensional array.
arr = np.array([1,2,3,4,5])
print(f"(1)--> One dimensional array is:- {arr}.")

# Creating two dimensional array.
arr1 = np.array([[1,2,3], [2,3,4]])
print(f"(2)---> Two dimensional array is:-\n {arr1}")

# Using the Built-In function to generate arrays.

arr2 = np.zeros((3,3))
print(f"(3)---> The array of size 3 by 3 in matrix form is:-\n {arr2}.")

# Creating the identity matrix.
arr3 = np.eye(4)
print(f"The identity matrix is:- \n {arr3}.")

# Or creating identity array or matrix using np.identity()function.
arr4 = np.identity(3)
print(arr4)

# Creating random array.

rand_array = np.random.rand(3,3) # Gives the 3 by 3 array consisting of random number between 0 and 1.
print(rand_array) 