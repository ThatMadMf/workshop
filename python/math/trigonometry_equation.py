import math


def calc(x):
    if x == 1:
        print('X cannot be 1. It causes zero division error in denominator X-1')
        return

    if math.cos(x) < 0:
        print('Cosine of X cannot be negative in sqrt(cos(X))')
        return

    if x == 7:
        print('X cannot be 7. It causes zero division error in denominator 7-X')
        return

    if x > 7:
        print('X cannot be more than 7 it causes illegal 0 or negative logarithm')
        return

    if x <= 3:
        print(f'Calculating sqrt(cos({x}) - arctg(7/({x} - 1))')
        result = math.sqrt((math.cos(x))) - math.atan(7 / (x - 1))
        print(f'Result is: {result}')
        return

    if x > 5:
        print(f'Calculating lg(1/(7-x))')
        result = math.log((1 / (7 - x)), 10)
        print(f'Result is: {result}')
        return


print('X value is out of function range')
repeat = True

while repeat:
    user_input = input('Enter X or press x to exit\n')

    if user_input in ['x', 'X']:
        repeat = False
    else:
        calc(int(user_input))
