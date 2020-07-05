k = int(input())
if (k % 2 == 0) or (k % 5 == 0):
    print('-1')
else:
    tmp = 1
    len = 1
    while (tmp % k != 0):
        tmp = tmp % k
        tmp = tmp * 10 + 1
        len += 1
    print(len)