t = eval(input())
for _ in range(t):
    n = eval(input())
    e = [int(x) for x in input().split()]
    a, b = e[0], 0
    for i in range(n - 1):
        a, b = e[i + 1] + b, max(a, b)
    print(max(a, b))
