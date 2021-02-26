def extract_negative(input_list):
    return [item for item in input_list if item < 0]


def extract_negative_loop(input_list):
    result = list()
    for item in input_list:
        if item < 0:
            result.append(item)
    return result


values = [1, 2, 6, -33, -233, 1, -5, -5]

print(f'Initial state of the list {values}')
print(f'Extract negative numbers via generator result: {extract_negative(values)}')
print(f'Extract negative numbers without generator result: {extract_negative_loop(values)}')
