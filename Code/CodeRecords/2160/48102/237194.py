def divide():
    dividend = int(input())
    divisor = int(input())
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend == -2**31:
            return 2**31-1
        else:
            return -dividend
    a, b = dividend, divisor
    sign = 1
    if a > 0 and b < 0 or a < 0 and b > 0:
        sign = -1
    a = a if a > 0 else -a
    b = b if b > 0 else -b
    res = div(a, b)
    return res * sign


def div(a, b):
    if a < b:
        return 0
    count = 1
    temp = b
    while temp + temp <= a:
        temp = temp + temp
        count = count + count
    return count + div(a - temp, b)


print(divide())