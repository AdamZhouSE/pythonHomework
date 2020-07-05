# 动态规划，根据邻居的距离计算自己的距离
matrix = []
try:
    while True:
        temp = input()
        line = [int(i) for i in temp.split(" ")]
        matrix.append(line)
except EOFError:
    pass
row = len(matrix)
column = len(matrix[0])
dist = []
for i in range(row):
    dist.append([100]*column)
for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            dist[i][j] = 0
        else:  # 从上到下 从左到右
            if i > 0:  # 不是在最上面一排
                dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
            if j > 0:
                dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
for i in range(row - 1, -1, -1):
    for j in range(column - 1, -1, -1):
        if i < row - 1:
            dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
        if j < column - 1:
            dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

for i in range(row):
    for j in range(column):
        if j == column-1:
            print(dist[i][j])
        else:
            print(dist[i][j],end=" ")
