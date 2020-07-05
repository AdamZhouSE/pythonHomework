'''
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
'''


def getSlope(x1, y1, x2, y2):
    slp = 0
    slp = (y1 - y2) / (x1 - x2)
    return slp


n = int(input())
x = []
y = []
for i in range(n):
    inp = input().split(',')
    x0 = int(inp[0])
    y0 = int(inp[1])
    x.append(x0)
    y.append(y0)
slp = []
for i in range(0, len(x) - 1):
    tmp = getSlope(x[i], y[i], x[i + 1], y[i + 1])
    slp.append(tmp)
t0 = slp[0]
ef = 0
for s in slp:
    if s != t0:
        ef = 1
        break
if ef == 0:
    print('True')
else:
    print('False')