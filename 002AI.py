import numpy as np

arr1 = np.random.rand(10, 10)
arr1 *= 100
arr1 = np.round(arr1)
print(arr1)
print()
print(f'Max num: {arr1.max()}; Position: {arr1.argmax()}')
print(f'Max num: {arr1.min()}; Position: {arr1.argmin()}')
print(f'Average: {np.round(arr1.mean())}')