def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

func = compose1(square, make_adder(2))
result1 = func(3)

##还有另外一种写法
result2 = compose1(square, make_adder(2))(3)

print(result1, result2)