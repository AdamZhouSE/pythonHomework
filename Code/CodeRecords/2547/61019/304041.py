read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    ns = read_line()
    k = read()
    ans = [k + n for n in ns]
    ok = set(ans)
    res = set()
    for k, v in enumerate(ns):
        if v in ok:
            loc = ans.index(v)
            if not loc == k:
                a = min(ns[loc], ns[k])
                b = max(ns[loc], ns[k])
                res.add((a, b))
    print(len(res))
