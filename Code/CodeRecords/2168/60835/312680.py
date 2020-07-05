n, m = map(int , input().split())
nodes = []

for x in range(n + 1):
    nodes.append([])
for x in range(m):
    u , v, w = map(int , input().split())
    nodes[u].append([v, w])
his = []
costs = [-1] * (n + 1)
result = []
def find(i, cost, start, road):
    global his, nodes, costs
    print(costs, i, start)
    if len(nodes[i]) == 0:
        return
    for x in nodes[i]:
        if x[0] == start:
            continue
        if x not in his:
            his.append(x)
            tem = cost
            tem = tem + x[1]
            if costs[x[0]] == -1:
                costs[x[0]] = tem
            else:
                costs[x[0]] = min(tem, costs[x[0]])
            find(x[0], tem, start, road)
res = []
for x in range(1, n + 1):
    his = []
    costs = [-1] * (n + 1)
    find(x, 0, x, [])
    del costs[0]
    del costs[x - 1]
    res.append(sum(costs))
minnum = 100000
for x in res:
    if x != -1:
        minnum = min(minnum, x)
if minnum == 100000:
    print(-1)
else:
    print(minnum)