t = eval(input())
for _ in range(t):
    n = eval(input())
    e = [int(x) for x in input().split()]
    i = 0
    r = []
    while i < n - 1:
        r.append(e[i + 1])
        r.append(e[i])
        i += 2
    if i == n - 1:
        r.append(e[-1])
    print(' '.join([str(x) for x in r]))
