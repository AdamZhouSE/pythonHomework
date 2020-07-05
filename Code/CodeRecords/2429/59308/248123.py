T = int(input())
for i in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    res = -1
    for j in range(n):
        for k in range(j):
            if a[k] <= a[j]:
                res = max(res, a[j]-a[k])
    print(res)
