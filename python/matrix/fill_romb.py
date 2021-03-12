import numpy as np

n = 9
matrix = np.diagflat([n, n, n, n], 3)
matrix = np.maximum(matrix, np.flip(matrix, 1))
matrix = np.maximum(matrix, np.flip(matrix, 0))

print(matrix)
