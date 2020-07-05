def reverse_integer(num):
    copy = num
    negative = False
    if num < 0:
        negative = True
        copy = -num
    res = 0
    while copy > 0:
        res = res * 10 + copy % 10
        copy //= 10
    if negative:
        return -res
    return res


print(reverse_integer(int(input())))