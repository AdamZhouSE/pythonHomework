"""
2.19
寻找黑色子矩阵
算出B的数量，可以求得边长
找到第一个B的位置，可以推出中心位置
"""
import math
inp = input().split()
n, m = int(inp[0]), int(inp[1])
data = []
count_b = 0
for i in range(0, n):
    line = list(input())
    for j in line:
        if j == "B":
            count_b += 1
    data.append(line)
position = []
is_first = 0
count_line = 0
for i in range(0, n):
    for j in range(0, m):
        if data[i][j] == "B":
            position = [i, j]
            for k in range(j, m):
                if data[i][k] == "B":
                    count_line += 1
            is_first = 1
            break
    if is_first == 1:
        break
# 求出边长
length = count_line
width = count_b // count_line
# 中心在矩阵的位置
mid_l = length // 2 + 1
mid_w = width // 2 + 1
# 由第一个坐标到中心,注意这里长加在列上，宽加在行上
position[0] += mid_w - 1
position[1] += mid_l - 1
# 数组首位是0，坐标从1开始
print(position[0]+1, position[1]+1)
