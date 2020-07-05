T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        tmp = 0
        for j in range(1, i + 1):
            tmp += j
        res += tmp
    print(res)
