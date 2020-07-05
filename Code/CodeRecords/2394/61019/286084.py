t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    r = []
    for e in es:
        r.append(e) if e else 0
    r.extend([0] * (n - len(r)))
    print(' '.join([str(x) for x in r])+' ')
