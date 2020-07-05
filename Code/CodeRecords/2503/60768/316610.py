N = int(input())
matrix = [[0 for x in range(N)] for y in range(N)]
# 邻接矩阵
edge = []
for i in range(N - 1):
    r, c = [int(x) - 1 for x in input().split(' ')]
    matrix[r][c] = 1
    matrix[c][r] = 1
    edge.append([r, c])
res = []


def dfs(node: int, path: list):
    flag = False
    for i in range(len(matrix[node])):
        if i not in path and matrix[node][i] == 1:
            flag = True
            break
    if not flag:
        res.append(len(path) - 1)
        return
    else:
        for j in range(N):
            if j not in path and matrix[node][j] == 1:
                path.append(j)
                dfs(j, path.copy())
                path = path[:-1]


for i in range(N):
    road = [i]
    dfs(i, road)

print(max(res))