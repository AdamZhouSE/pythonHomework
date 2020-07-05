N, M = [int(x) for x in input().split()]
edges = []  # 边集
vertices = [[i] for i in range(1, N+1)]  # 点集
for i in range(M):
    a, b, L = [int(x) for x in input().split()]
    edges.append([L, a, b])
edges.sort()  # 边按长度升序排列
nums = []  # 用来存储已选边变长


def kruskal():
    for i in range(N-1):
        while True:  # 选边
            edge = edges[0]
            start = edge[1]
            end = edge[2]
            m, n = [[], []]
            for part in vertices:
                if start in part:
                    m = part
                if end in part:
                    n = part
            if m == n:
                edges.pop(0)
                continue
            else:
                ind1 = vertices.index(m)
                ind2 = vertices.index(n)
                vertices[ind1].extend(vertices[ind2])
                vertices.pop(ind2)  # 合并连通分量
                nums.append(edge[0])
                edges.pop(0)
                break


kruskal()
print(max(nums), end='')