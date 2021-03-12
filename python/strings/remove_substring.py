base_string = input('Enter base string\n')
substring = input('Enter substring\n')

result_string = ''.join([c for c in base_string if c not in substring])

print(result_string)
