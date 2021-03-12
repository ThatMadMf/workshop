string_value = input('Enter string value:\n')
chars = input('Enter chars separated with space:\n').split()

for c in chars:
    print(f'Character {c} has {string_value.count(c)} occurrences')
