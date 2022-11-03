def next_largest_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    else:
        return None
    
def last_lower_coin(coin):
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1
    else:
        return None

def find_near(n):
    if n >= 25:
        return 25
    elif n >= 10:
        return 10
    elif n >= 5:
        return 5
    else:
        return 0

def count_partitions(n):
    m = find_near(n)
    n = last_lower_coin(m)