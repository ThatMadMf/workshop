chars = input('Enter symbols separated via space\n').split()
char_occur = {}

for c in chars:
    if c in char_occur:
        char_occur[c] = char_occur[c] + 1
    else:
        char_occur[c] = 1
result_chars = [c for c, v in char_occur.items() if v == max(char_occur.values())]

symbols = list()
indexes = list()

for i, c in enumerate(chars):
    if c in result_chars:
        symbols.append(c)
        indexes.append(i)

print(f'{symbols}\n{indexes}')
