import numpy as np

# Creating a 1-dimensional array
arr1 = np.array([1, 2, 4])
print(arr1)

# Creating a 2-dimensional array
arr2 = np.array([[1, 2, 3, 5], [8, 4, 9, 7]])
print("\nArray 2:")
print(arr2)

# Creating a 3-dimensional array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])
print(arr3)

arr3d_2 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

# Adding two 3D arrays
array_sum = arr3 + arr3d_2
print("The sum of two arrays is:")
print(array_sum)

# Create a 3x3 matrix of zeros
zero = np.zeros((3, 3))
print(zero)

# Create a 4x4 matrix of ones
one = np.ones((4, 4))
print(one)

# To print a random matrix in numpy
random_matrix = np.random.random((4, 4))
print(random_matrix)

# Array Operator
# Array operator is used to perform calculations between arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# To perform sum between these two arrays we use +
sum_arr = arr1 + arr2
print(sum_arr)

# To perform difference between these two arrays we use -
dif_arr = arr1 - arr2
print(dif_arr)

# To perform multiplication between these two arrays we use *
multiply_arr = arr1 * arr2
print(multiply_arr)

# To perform division between these two arrays we use /
div_arr = arr1 / arr2
print(div_arr)

# Now slicing topic of array
slic = np.array([1, 2, 3, 4, 5])
# To slice data up to the 3rd index from 0 so it will reach up to the 2nd index, counting up to three data
print(slic[:3])

# Original array
re_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape the array to 2x4
re_shared_array = re_array.reshape((2, 4))
print(re_shared_array)

# To aggregate data in numpy we use functions such as sum, mean, std
example_arr = np.array([30, 40, 40, 50, 70])

sum_arr = np.sum(example_arr)
print(sum_arr)

#using scaler value to manipulate numpy array
scaler = 20

sum_scaler = scaler + arr2
print(sum_scaler)

#for multyplying
mul_scaler = scaler * arr3

#to generate matrix transpose value of numpy array
trans = np.transpose(arr3)
print(trans)