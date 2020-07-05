n = int(input())
edge = [0, 0]*n
for x in range(n - 1):
    u, v, w = map(int, input().split())
    edge[u] = [v, w]
for x in range(int(input())):
    u, v = map(int, input().split())
    now = u
    res = 0
    while now != v:
        #print(res, end = ' ')
        res = res ^ edge[now][1]
        now = edge[now][0]
    print(res)
        