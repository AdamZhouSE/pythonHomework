T = int(input())
for hhh in range(0, T):
    n = int(input().split()[2])
    uList = [int(i) for i in input().split()]
    vList = [int(i) for i in input().split()]
    res = [(u, v) for u in uList for v in vList if u + v == n]
    res.sort()
    if not res:
        print(-1)
    for i in res:
        print(i[0], i[1])