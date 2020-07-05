T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = 1
    tmp = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tmp += i
    if tmp >= 2 * n:
        res = 0
    print(res)
