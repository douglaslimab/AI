import numpy as np

arr1 = np.arange(1, 11)
arr1[8:10] = 33
print(arr1)
print(arr1[2:6])
print(arr1[:5])
print(arr1[5:])