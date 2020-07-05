t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = []
    for i in range(n-1):
        if a[i]>a[i+1]:
            res.append(str(a[i+1]))
        else:
            res.append("-1")
    res.append("-1")
    print(' '.join(res),'')