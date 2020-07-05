n, k = [int(x) for x in input().split()]
edges = []  # 边集
vertices = [[i] for i in range(1, n+1)]  # 点集
for i in range(k):
    a, b, m = [int(x) for x in input().split()]
    edges.append([m, a, b])
edges.sort()  # 边按长度升序排列
ans = 0


def kruskal():
    global ans
    for i in range(n-1):
        while True:  # 选边
            edge = edges[0]
            start = edge[1]
            end = edge[2]
            x, y = [[], []]
            for part in vertices:
                if start in part:
                    x = part
                if end in part:
                    y = part
            if x == y:
                ans += edge[0]
                edges.pop(0)
                continue
            else:
                ind1 = vertices.index(x)
                ind2 = vertices.index(y)
                vertices[ind1].extend(vertices[ind2])
                vertices.pop(ind2)  # 合并连通分量
                edges.pop(0)
                break


kruskal()
for i in edges:
    ans += i[0]
print(ans, end='')