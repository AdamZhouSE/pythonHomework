t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split(' ')]
    lbig = [-1e18] * n
    rsmall = [1e18] * n
    for k, v in enumerate(a):
        lbig[k] = max(lbig[k - 1], v) if k else v
    for k, v in enumerate(reversed(a)):
        rsmall[k] = min(rsmall[k - 1], v) if k else v
    for k, v in enumerate(a[1:-1]):
        if lbig[k] <= v <= rsmall[n - 3 - k]:
            print(v)
            break
    else:
        print(-1)
