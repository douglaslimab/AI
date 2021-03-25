import numpy as np

arr1 = np.random.randint(0, 9, (3, 2))
print(arr1)
arr2 = np.random.randint(10, 19, (2, 3))
print(arr2)
arr0 = np.matmul(arr1, arr2)
print(arr0)
print(arr0.sum())