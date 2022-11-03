"""First python source file"""
from operator import floordiv, mod

def divide_exact(a, b):
    return floordiv(a, b), mod(a, b)

q, r = divide_exact(2022, 10)
print('Quotient: ', q)
print('Remainder: ', r)

"""Return the absolute value of x"""
def absolute_value(x):
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return 0

a = absolute_value(-3)
print(a)