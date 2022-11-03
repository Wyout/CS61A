def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

def for_sum(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total