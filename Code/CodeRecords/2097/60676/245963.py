def func(numerator, denominator):
    integer = numerator // denominator
    numerator %= denominator
    if numerator == 0:
        return integer
    gcd = 1
    for i in range(numerator):
        if denominator % (numerator-i) == 0 and numerator % (numerator-i) == 0:
            gcd = numerator-i
            break
    numerator //= gcd
    denominator //= gcd
    denominator_copy = denominator
    while denominator_copy % 2 == 0:
        denominator_copy //= 2
    while denominator_copy % 5 == 0:
        denominator_copy //= 5
    res = '' + str(integer) + '.'
    if denominator_copy == 1:
        numerator_copy = numerator
        while numerator_copy > 0:
            res += str(10 * numerator_copy // denominator)
            numerator_copy = 10 * numerator_copy % denominator
    else:
        numerator_copy = numerator
        reminder = []
        while numerator_copy not in reminder:
            reminder.append(numerator_copy)
            res += str(10 * numerator_copy // denominator)
            numerator_copy = 10 * numerator_copy % denominator
        repeat_length = len(reminder) - reminder.index(numerator_copy)
        res = res[:-repeat_length] + '(' + res[-repeat_length:] + ')'
    return res


print(func(int(input()), int(input())))