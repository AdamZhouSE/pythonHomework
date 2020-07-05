t = eval(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    es = [int(x) for x in input().split()]
    es.reverse()
    fs = [abs(e - k) for e in es]
    r = es[fs.index(min(fs))]
    print(r)
