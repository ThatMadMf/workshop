import numpy as np

base_array = list(map(int, input('Enter base array\n').split(' ')))
indexes = list(map(int, input('Enter array of indexes\n').split(' ')))

matrix = np.asarray(base_array)

print(f'Result: {matrix[indexes]}')
