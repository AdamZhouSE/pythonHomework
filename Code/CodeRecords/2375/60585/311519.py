N, M = [int(x) for x in input().split()]
edges = []  # 边集
vertices = [[i] for i in range(1, N+1)]  # 点集
for i in range(M):
    a, b, L = [int(x) for x in input().split()]
    edges.append([L, a, b])
edges.sort()  # 边按长度升序排列
nums = []  # 用来存储已选边变长