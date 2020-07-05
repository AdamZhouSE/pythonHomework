def divide(dividend, divisor):
    if divisor == 0:
        return None
    if dividend == 0:
        return 0
    negative = False
    if divisor < 0 < dividend:
        divisor = -divisor
        negative = True
    if dividend < 0 < divisor:
        dividend = -dividend
        negative = True
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if negative:
        return -quotient
    return quotient


print(divide(int(input()), int(input())))