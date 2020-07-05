import math

# 先求最小生成树，再删除S-1条最大的边
S, P = [int(x) for x in input().split()]
edges = []  # 边集
tree = []  # 最小生成树的边
info = []  # 存储边坐标
vertices = [[i] for i in range(P)]  # 连通分量
for i in range(P):
    info.append([int(x) for x in input().split()])
for i in range(P):
    for j in range(P):
        if i == j:
            continue
        x1, y1 = info[i]
        x2, y2 = info[j]
        edges.append([math.sqrt((x1-x2)**2 + (y1-y2)**2), i, j])
edges.sort()  # 按距离从小到大排序
for i in range(P-1):  # 构造最小生成树
    while True:
        edge = edges[0]
        start = edge[1]
        end = edge[2]
        m, n = [0, 0]
        for part in vertices:
            if start in part:
                m = part
            if end in part:
                n = part
        if m == n:
            edges.pop(0)
            continue
        tree.append(edge[0])
        ind1 = vertices.index(m)
        ind2 = vertices.index(n)
        vertices[ind1].extend(vertices[ind2])
        vertices.pop(ind2)
        edges.pop(0)
        break
for i in range(S-1):
    max_path = max(tree)
    tree.remove(max_path)
res = max(tree)
if res == int(res):
    print(str(int(res))+".00", end='')
else:
    print(round(res, 2), end='')
