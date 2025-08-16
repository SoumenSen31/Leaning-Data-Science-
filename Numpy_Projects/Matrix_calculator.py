import numpy as np 
arr1_2d = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])

arr2_2d = np.array([[9, 8, 7], 
                    [6, 5, 4], 
                    [3, 2, 1]])

def sum_arr(a, b):
    return np.add(a, b)

def sub(a, b):
    return np.subtract(a, b)

def mul(a, b):
    return np.matmul(a, b)

def my_transpose(a):
    return np.transpose(a)

def determinant(a):
    return np.linalg.det(a)

print(f'addition: \n{sum_arr(arr1_2d,arr2_2d)}')
print(f'Substraction: \n{sub(arr1_2d, arr2_2d)}')
print(f'Multiplication: \n{mul(arr1_2d, arr2_2d)}')
print(f'transpose of arr_1:  \n{my_transpose(arr1_2d)}', end ="\n"f'transpose of arr_2: \n{my_transpose(arr2_2d)}\n')
print(f'determinant of arr_1:  \n{determinant(arr1_2d)}', end ="\n"f'determinant of arr_2: \n{determinant(arr2_2d)}')