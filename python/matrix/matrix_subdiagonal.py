import numpy as np

k = int(input('Enter k\n'))
matrix = np.zeros([k, k])
rng = np.arange(k - 1)

matrix[rng, rng + 1] = 9
matrix[rng, rng - 1] = 9

print(matrix)
