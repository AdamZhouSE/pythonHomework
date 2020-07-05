t = eval(input())
for _ in range(t):
    n = eval(input())
    e = [int(x) for x in input().split()]
    x = eval(input())
    ts = [(a, b, x - (e[a] + e[b])) for a in range(n) for b in range(n) if a < b]
    ys = [(a, b, e[a] + e[b]) for a in range(n) for b in range(n) if a < b]
    for t in ts:
        for y in ys:
            if (
                    t[2] == y[2] and
                    t[0] != y[0] and
                    t[0] != y[1] and
                    t[1] != y[0] and
                    t[1] != y[1]):
                print(1)
                exit(0)
    print(0)