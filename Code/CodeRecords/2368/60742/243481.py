t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = []
    while a:
        if len(a)==1:
            res.append(str(a[0]))
            a.pop(0)
            continue
        res.append(str(a[-1]))
        a.pop()
        res.append(str(a[0]))
        a.pop(0)
    print(' '.join(res))