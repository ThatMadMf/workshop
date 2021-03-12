import numpy as np

base_array = list(map(int, input('Enter base array\n').split(' ')))

matrix = np.asarray(base_array)
input_value = input('Enter condition with format: "[more or less than sign] [number]"\n').split(' ')

is_bigger = input_value[0] == '>'
border_number = int(input_value[1])

print(f'Result matrix is:\n{matrix[matrix > border_number] if is_bigger else matrix[matrix < border_number]}')
