T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    res = []
    for i in range(1, n+1):
        s = 0
        for k in range(0, n-i+1):
            s = max(s, min(a[k:k+i]))
        res.append(s)
    print(*res)

