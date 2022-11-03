"""Print the prime factors of n in non-decreasing order"""

def prime_factors(n):
    i = smallest_prime_factor(n)
    while n > 1:
        n = n // i
        print(i)

def smallest_prime_factor(n):
    i = 2
    while n % i != 0:
        i = i + 1
    return i
