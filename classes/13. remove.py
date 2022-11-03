def remove(n, digit):
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept +last * 10 ** digits 
            digits = digits + 1
    return kept

result = remove(123, 2)
print(result)