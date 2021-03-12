def count_substring(input, match_value):
    occurrences = 0
    for i in range(len(input) - len(match_value)):
        if input[i:i+len(match_value)] == match_value:
            occurrences += 1

    return occurrences


string_value = input('Enter string value\n')
substring = input('Enter substring\n')

print(f'Count of occurrences is {count_substring(string_value, substring)}')
