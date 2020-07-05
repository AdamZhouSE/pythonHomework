# Dijkstra算法,不会改变邻接矩阵里面的数据，若改变循环
# 会发生错误
import numpy as np

line = input().split(" ")
line = [int(x) for x in line]
n = line[0]
m = line[1]
s = line[2] - 1
t = line[3] - 1
mat_origin = [99999] * (n * n)
result = [-1] * n  # 记录最短路径长度
vertices = [-1] * n  # 已经求出到这个点的最短路径，记录这个点的标号
mat = np.array(mat_origin).reshape(n, n)
for i in range(n):
    mat[i][i] = 0
for i in range(m):
    temp = input().split(" ")
    temp = [int(x) for x in temp]
    x = temp[0] - 1
    y = temp[1] - 1
    value = temp[2]
    mat[x][y] = mat[y][x] = value
vertices[s] = s
result = mat[s].copy()
# 找最短路径
for i in range(n - 1):
    min = 99999
    index = s
    for j in range(n):
        if vertices[j] == -1 and result[j] < min:
            min = result[j]
            index = j  # 最新更新入最短路径的点
    vertices[index] = index
    # 绕当前的点去更新最短路径
    for k in range(n):
        # 如果已经求出了最短路径，并且经过那个点绕之后比当前的路径短，就更新
        if vertices[k] == -1 and mat[index][k] < 99999 and result[k] > result[index] + mat[index][k]:
            result[k] = result[index] + mat[index][k]
print(result[t])
