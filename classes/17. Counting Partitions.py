def count(n, m):
    if n == 0:#基础条件可以不止一个
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count(n-m, m)
        without_m = count(n, m-1)
        return with_m + without_m