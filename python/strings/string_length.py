string_value = input('Enter string value\n')

print(f'There are/is {len([c for c in string_value if c.isdigit()])} numbers in the string')
