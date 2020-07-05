t = eval(input())
for _ in range(t):
    n, m, x = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    for u in range(n):
        for v in range(m):
            if a[u] + b[v] == x:
                print(a[u], b[v])
