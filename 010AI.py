import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
# get a specific element
print(a[1, 5])
# get specific row
print(a[0, :])
# get specific column
print(a[:, 2])
# get an interval in a row skipping 2
print(a[0, 1:6:2])
# get an interval in a row skipping -1
print(a[1, 6:1:-1])
# replacing one element
a[0, 6] = 99
print(a)
# replacing one column
a[:, 4] = [66, 55]
print(a)