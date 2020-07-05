li = input().strip().split(" ")
n = int(li[0])
m = int(li[1])
L = int(li[2])
values = [int(i) for i in input().strip().split(" ")]
edges = []
for i in range(n):
    e = []
    for j in range(n):
        e.append(999999)
    edges.append(e)
for i in range(m):
    li = input().strip().split(" ")
    edges[int(li[0]) - 1][int(li[1]) - 1] = edges[int(li[1]) - 1][int(li[0]) - 1] = int(li[2])

# 更新各条路径上的最短路径
for t in range(n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(n):
                if k != i and k != j and max(edges[i][k], edges[k][j]) < edges[i][j]:
                    edges[i][j] = max(edges[i][k], edges[k][j])

pairs = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if abs(values[i] - values[j]) >= L:
            pairs.append([i, j])
result = 0
for p in pairs:
    result += edges[p[0]][p[1]]
print(result)