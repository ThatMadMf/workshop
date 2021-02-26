values = [1, 2, 6, -33, -233, 1, -5, -5]
index = 3
element = -69

print(f'Initial state of the list {values}')
print(f'Index to insert is {index}')
print(f'Element to insert is {element}')
print(f'Result of insert: {values[:index] + [element] + values[index:]}')
