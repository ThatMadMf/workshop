def get_line(number):
    if number == 0:
        return ''
    return f'{get_line(number - 1)}| {number}  | '


n = int(input('Enter amount of letters that should be drawn\n'))
print(' ___   ' * n)
print('|   \\  ' * n)
print(get_line(n))
print('|___/  ' * n)
print('|      ' * n)
print('|      ' * n)
