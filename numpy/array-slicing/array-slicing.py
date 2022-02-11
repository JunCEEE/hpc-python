import numpy as np

arr = np.random.rand(4, 4)
print(arr[1, :])
print(arr[:, 2])
arr[:2, :2] = 0.21
print(arr)

chequerboard = np.array([[1, 0] * 4, [0, 1] * 4] * 4)
print(chequerboard)
