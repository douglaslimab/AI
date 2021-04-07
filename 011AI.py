import numpy as np

mat = np.array([[[1, 2],
                 [3, 4]],
                [[5, 6],
                 [7, 8]]])

print(mat)
print(mat[0, 1, 1])
print(mat[1, 0, :])
print(mat[1, :, :])
mat[:, 1, :] = [[9, 9], [8, 8]]
print(mat)