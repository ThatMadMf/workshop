def calc_denominator(i, x):
    result = 1
    is_negative = False
    for j in range(i, 0, -1):
        result *= (x - j) if is_negative else (x + j)
        is_negative = not is_negative

    if result == 0:
        print('Invalid input. Denominator in one or multiple elements of sequence is zero. Try input where x > n')
        quit(1)

    return result


def calc_seq_for(n, x):
    result = 0
    for i in range(n):
        current_denominator = calc_denominator(i + 1, x)
        if i % 2 == 0:
            result += (n - i) / current_denominator
        else:
            result -= (n - i) / current_denominator
    return result


def calc_seq_while(n, x):
    result = 0
    i = 0
    while i != n:
        current_denominator = calc_denominator(i + 1, x)
        if i % 2 == 0:
            result += (n - i) / current_denominator
        else:
            result -= (n - i) / current_denominator
        i += 1
    return result


def calc_seq_recursion(n, x, depth):
    if depth == n:
        return n / calc_denominator(1, x)
    denominator = calc_denominator(n - depth + 1, x)
    element_index = n - depth
    current_value = (depth / denominator) if element_index % 2 == 0 else (depth / denominator * -1)

    return current_value + calc_seq_recursion(n, x, depth + 1)


n_input = int(input('Enter n\n'))
x_input = int(input('Enter x\n'))

print(f'Sequence calculated via for: {calc_seq_for(n_input, x_input)}')
print(f'Sequence calculated via while: {calc_seq_while(n_input, x_input)}')
print(f'Sequence calculated via recursion: {calc_seq_recursion(n_input, x_input, 1)}')
