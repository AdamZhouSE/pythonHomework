t = eval(input())
for _ in range(t):
    n, k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    r = []
    for i in range(0, n, k):
        sa = a[i:i + k]
        r.extend(sa[::-1])
    print(' '.join([str(sr) for sr in r]) + ' ')
