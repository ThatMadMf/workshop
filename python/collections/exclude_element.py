def extract_element(input_list, element):
    return [item for item in input_list if item != element]


def extract_element_loop(input_list, element):
    result = list()
    for item in input_list:
        if item != element:
            result.append(item)
    return result


values = [1, 2, 6, -33, -233, 1, -5, -5]
n = 1

print(f'Initial state of the list {values}')
print(f'N is {n}')
print(f'Extract {n} via generator result: {extract_element(values, n)}')
print(f'Extract {n} without generator result: {extract_element_loop(values, n)}')
