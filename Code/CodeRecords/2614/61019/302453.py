read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    a = read_line()
    b = read_line()
    c = read_line()
    res = {}
    for i in range(n):
        v = a[i] - b[i]
        res[v] = res[v] + 1 if v in res else 1
    print(sum([res[x] for x in c if x in res]))
