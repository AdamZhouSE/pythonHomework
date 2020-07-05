# 题目描述
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，
# 其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
#
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，
# 是则返回 true，否则请返回 false。

n = int(input())
li = []
for i in range(n):
    k = input().strip().split(",")
    t = [int(k[0]), int(k[1])]
    li.append(t)

x1 = li[0][0]
y1 = li[0][1]
x2 = li[1][0]
y2 = li[1][1]

k = 0
if x1 != x2:
    k = (y1-y2)/(x1-x2)
b = y1-k*x1
if n == 2:
    print("True")
else:
    isOK = True
    for i in range(3, n):
        y = li[i][1]
        x = li[i][0]
        if (y != k*x+b):
            isOK = False
            break
    print(isOK)