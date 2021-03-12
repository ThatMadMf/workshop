import re


def is_index(input):
    return re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", input)


string_value = input('Enter string value\n')

print(f'{string_value} is an index' if is_index(string_value) else f'{string_value} is not an index')
