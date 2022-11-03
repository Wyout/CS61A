def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:#递归函数中最好有一个基础条件，比如这里的if
        return n
    else:#然后再有个执行，这样方便读代码
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit