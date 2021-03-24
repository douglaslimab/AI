import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr3 = np.arange(0, 10)
arr4 = np.arange(0, 10, 2)

arr5 = np.zeros(5)

arr6 = np.ones(4)
arr7 = np.ones((3, 4))

arr8 = np.eye(5)

arr9 = np.linspace(0, 10, 3)
arr10 = np.linspace(0, 10, 4)

arr11 = np.random.rand(5)
arr12 = np.random.rand(3, 4)

arr13 = np.random.uniform(3, 7, 10)
arr14 = np.random.uniform(3.5, 11.47, (3, 2))

arr15 = np.random.randint(5, 13)
arr16 = np.random.randint(5, 13, 7)
arr17 = np.random.randint(5, 13, (3, 4))

print(arr17)
print(arr17.shape)
print(arr17.reshape(2, 6))
print(arr17)