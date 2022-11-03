def missing_digits(n):
    if n < 10:
        return 0
        
    else:
        last = n % 10
        last_but_two = n // 10 % 10
        if last != last_but_two:
            count = last - last_but_two - 1
            return count + missing_digits(n//10)
        else:
            return missing_digits(n//10)