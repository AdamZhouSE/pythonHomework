t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    print(int(n * (n + 1) / 2 - sum(es)))
