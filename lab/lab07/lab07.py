from audioop import mul


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # for i in it:
    #     yield i * multiplier
    new_it = map(lambda x: x * multiplier, it)
    yield from new_it

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # normal
    while True:
        yield n
        if n == 1:
            break
        if n%2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
    
    # recursion
    yield n
    if n % 2 == 0:
        yield from hailstone(n//2)
    elif n % 2 == 1 and n != 1:
        yield from hailstone(n*3 + 1)

    # 没有n == 1的原因是：
    # yield结束的条件是后续再也没有yield
    # 所以最后弄到了n = 1是，if 和 elif都没法进行，就自动停止生成了

    # 如果要写n == 1的情况，也可以，就是要在每个if(eilf)下面写一个yield 