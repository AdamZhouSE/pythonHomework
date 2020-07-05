t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = []
    for i in range(n):
        exist = False
        for j in range(i+1,n):
            if a[j]>=a[i]:
                exist = True
                res.append(str(a[j]))
                break
        if not exist:
            res.append('-1')
    print(' '.join(res))