# 计算功能
def add_rational(x, y):
    # 赋值可有可不有
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    print(numer(x), "/", denom(x))

# 构造功能
import math
def rational(n, d):
    g = math.gcd(n, d)
    n, d = n//g, d//g
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')