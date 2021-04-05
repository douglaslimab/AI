import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print(a[1, 5])
print(a[0, :])
print(a[:, 2])
print(a[0, 1:6:2])
print(a[1, 6:1:-1])
print()