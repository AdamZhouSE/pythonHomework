def walk(G, s, S = set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u - 1].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


info = input().split()
info = [int(x) for x in info]
node_nums = info[0]
node_root = info[1]
node_relation_list = []
for i in range(1, node_nums + 1):
    node_relation_list.append(set())
node_weight = []
for i in range(node_nums):
    node_weight.append(0)
for i in range(node_nums):
    info = input().split()
    info = [int(x) for x in info]
    node_relation_list[info[0] - 1].add(info[1])
    node_relation_list[info[0] - 1].add(info[2])
    node_weight[info[0] - 1] = info[3]
P = walk(node_relation_list, node_root)
goal = int(input())
valid_list = []
for i in range(1, node_nums + 1):
    startNode = i
    temp = []
    res = 0
    while P[startNode] is not None:
        temp.append(startNode)
        res = res + node_weight[startNode - 1]
        if res == goal:
            valid_list.append(len(temp))
        startNode = P[startNode]
    temp.append(startNode)
    res = res + node_weight[startNode - 1]
    if res == goal:
        valid_list.append(len(temp))
maxPath = max(valid_list)
print(maxPath)