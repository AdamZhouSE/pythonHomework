n, m = map(int, input().strip().split(" "))
graph = [[0 for i in range(0, n + 1)] for j in range(0, n + 1)]
for i in range(0, m):
    x, y, weight = map(int, input().strip().split(" "))
    graph[x][y] = weight
    graph[y][x] = weight
print(graph)
vertices = list(range(1, n + 1))
while True:
    k = len(vertices)
    for num in vertices:
        if graph[num].count(0) == n:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == num or j == num:
                        graph[i][j] = 0
            vertices.remove(num)
            break
    if k == len(vertices):
        break
    else:
        continue
result = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        result = max(result, graph[i][j])
print(result)
