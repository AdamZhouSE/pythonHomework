t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = []
    for i in range(n):
        leader = True
        for j in range(i+1,n):
            if a[i]<a[j]:
                leader = False
                break
        if leader:
            res.append(str(a[i]))
    print(' '.join(res))