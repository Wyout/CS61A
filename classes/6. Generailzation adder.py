"""Generalization3"""
def make_adder(n):
    def adder(k):
        return n + k
    return adder

a = make_adder(2020)(2)
f = make_adder(2020)
b = f(2)
print(a, b)