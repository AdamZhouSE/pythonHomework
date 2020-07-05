t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ad = dict([(x, 0) for x in a])
    bd = dict([(x, 0) for x in b])
    for x in a:
        ad[x] += 1
    for x in b:
        bd[x] += 1
    print(1 if ad == bd else 0)
