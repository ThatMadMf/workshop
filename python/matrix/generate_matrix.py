import numpy as np

m = int(input('Enter m\n'))
n = int(input('Enter n\n'))

matrix = np.empty([m, n])
matrix.fill(0.5)
np.fill_diagonal(matrix, -1)

print(f'Generated matrix: \n{matrix}')
