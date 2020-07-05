"""
首位两棵树一定符合
求出相邻坐标之间的差与中间的树的高
"""
n = int(input())
# 首尾符合
count = 2
data = []
data_h = []
data_dif = []
for i in range(n):
    inp = input().split(" ")
    x, h = int(inp[0]), int(inp[1])
    data_h.append(h)
    data.append([x, h])
# 去掉首尾两棵树
del data_h[0], data_h[-1]
# 相邻两个坐标的差
for i in range(0, n-1):
    data_dif.append(data[i+1][0]-data[i][0])
for i in range(len(data_h)):
    # 向左倒
    if data_h[i] < data_dif[i]:
        count += 1
    # 向右倒
    elif data_h[i] < data_dif[i+1]:
        count += 1
        data_dif[i+1] -= data_h[i]
print(count)
