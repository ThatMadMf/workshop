import numpy as np

m = int(input('Enter m\n'))
n = int(input('Enter n\n'))

matrix = np.empty([m, n])
matrix.fill(0.5)
np.fill_diagonal(matrix, -1)

print(f'Generated matrix: \n{matrix}')

left_index = list(map(int, input('Enter coordinates of top left corner\n').split(' ')))
right_index = list(map(int, input('Enter coordinates of bottom right corner\n').split(' ')))

print(f'Selected matrix chunk:\n {matrix[np.ix_(left_index, right_index)]}')
