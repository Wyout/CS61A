def fib(n):
    cur, pre = 0, 1
    k = 0
    while k < n: 
        cur, pre = pre, cur + pre
        k = k + 1
    return cur
a = fib(0)
b = fib(4)
print(a, b)