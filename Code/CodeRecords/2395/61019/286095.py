t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    r = []
    for k, v in enumerate(es):
        if not v:
            continue
        if k < n - 1 and v == es[k + 1]:
            r.append(2 * v)
            es[k + 1] = 0
        else:
            r.append(v)
    r.extend([0] * (n - len(r)))
    print(' '.join([str(x) for x in r]))
