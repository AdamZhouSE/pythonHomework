"""
曼哈顿距离 |x1-x2|+|y1-y2|
欧式距离 sqrt[(x1-x2)^2+(y1-y2)^2]
两者相等
即 x1-x2=0 或者 y1-y2=0
"""
n = int(input())
data = []
for i in range(n):
    inp = [int(x) for x in input().split(" ")]
    data.append(inp)
res = 0
for i in range(n-1):
    x1 = data[i][0]
    y1 = data[i][1]
    for j in range(i+1, n):
        x2 = data[j][0]
        y2 = data[j][1]
        if x1-x2 == 0 or y1-y2 == 0:
            res += 1
print(res)
