def count_stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return count_stair_ways(n - 2) + count_stair_ways(n - 1)

def count_k(n, k):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        total = 0
        i = 1
        #如果没要求，不要死磕不用 while for等 的情况
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    
    return [x * s.index(x) for x in s if s.index(x) % 2 == 0]

def max_product(s):
    """
    Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1

    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))