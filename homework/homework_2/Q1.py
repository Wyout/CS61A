def num_eights(x):
    if x == 0:
        return 0
    else:
        if x % 10 == 8:
            return 1 + num_eights(x // 10)
        else:
            return 0 + num_eights(x // 10)

