import math
import matplotlib.pyplot as plt

import numpy as np


def calc_first(x):
    if x == 1:
        return None
    if math.cos(x) < 0:
        return None
    if x <= 3:
        return math.sqrt((math.cos(x))) - math.atan(7 / (x - 1))
    return None


def calc_second(x):
    if x >= 7:
        return None
    if x > 5:
        return math.log((1 / (7 - x)), 10)
    return None


a = int(input('Enter a: \n'))
b = int(input('Enter b: \n'))
xs = np.arange(start=a, stop=b, step=0.5)

calc_first_func = np.vectorize(lambda x: calc_first(x))
y1 = calc_first_func(xs).astype(np.double)
y1mask = np.isfinite(y1)

calc_second_func = np.vectorize(lambda x: calc_second(x))
y2 = calc_second_func(xs).astype(np.double)
y2mask = np.isfinite(y2)

plt.plot(xs[y1mask], y1[y1mask], linestyle='-', marker='o')
plt.plot(xs[y2mask], y2[y2mask], linestyle='-', marker='o')


plt.show()
