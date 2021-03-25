import numpy as np

arr1 = np.random.randint(1, 4, (3, 3))
print(arr1)
print(arr1.sum(axis=0))
print(arr1.sum(axis=1))