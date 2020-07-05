T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        res += i * i
    print(res)
