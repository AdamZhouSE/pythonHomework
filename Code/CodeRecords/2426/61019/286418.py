t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    ne = [e for e in es if e < 0]
    po = [e for e in es if e > 0]
    ne.sort(reverse=True)
    po.sort(reverse=True)
    m1 = po[0] * po[1] * po[2] if len(po) >= 3 else -1e18
    m2 = po[0] * ne[0] * ne[1] if len(po) >= 0 and len(ne) >= 2 else -1e18
    m3 = po[0] * po[1] * ne[0] if len(po) == 2 and len(ne) == 1 else -1e18
    print(max([m1, m2, m3]))
