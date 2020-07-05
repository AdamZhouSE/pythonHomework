t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    es.append(0)
    r = []
    for i in range(n):
        r.append(es[i] ^ es[i + 1])
    print(' '.join([str(x) for x in r]))