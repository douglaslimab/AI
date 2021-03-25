import numpy as np

arr1 = np.random.randint(1, 100, (3, 3))
arr2 = np.eye(3)
arr0 = arr1 * arr2

print(arr1)
print(arr2)
print(arr0)