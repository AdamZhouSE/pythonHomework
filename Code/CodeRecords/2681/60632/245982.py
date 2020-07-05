t = int(input())
res = []
for i in range(t):
    n = int(input())
    times = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
            times += 1
        else:
            n -= 1
            times += 1
    res.append(times)
for i in res:
    print(i)
