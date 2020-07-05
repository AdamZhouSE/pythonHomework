T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = ''
    for i in range(1, n + 1):
        b = bin(i)
        tmp = b[2:len(b)]
        res += tmp + ' '
    print(res)
