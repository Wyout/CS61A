def num_eights(x):
    if x == 0:
        return 0
    else:
        if x % 10 == 8:
            return 1 + num_eights(x // 10)
        else:
            return 0 + num_eights(x // 10)
"""
用while来提供思路

def pingpong_demo(n):
    index, ppn, dir = 1, 1, 1
    while index != n:
        index += 1
        ppn += dir
        if (index % 8) == 0 or num_eights(index) != 0:
            dir = -dir
    return ppn
"""

def helper(index, ppn, dir, n):
    if index != n:
        if (index % 8) == 0 or num_eights(index) != 0:
            return helper(index+1, ppn-dir, -dir, n)
            #用这种方式来代替赋值，同时注意此时的ppn-dir
        else:
            return helper(index+1, ppn+dir, dir, n)
    else:
        return ppn

def pingpong(n):
    return helper(1, 1, 1, n)
