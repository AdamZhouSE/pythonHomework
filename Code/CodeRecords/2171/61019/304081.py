read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    ns = read_line()
    fs = [1 if n % 2 else 0 for n in ns]
    r = []
    for i in range(n):
        if not fs[i]:
            r.append(ns[i])
    for i in range(n):
        if fs[i]:
            r.append(ns[i])
    print(' '.join([str(n) for n in r])+' ')
