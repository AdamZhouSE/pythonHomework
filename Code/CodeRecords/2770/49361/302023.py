t = int(input())


class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index


res = []
digit = [-1 for i in range(10000)]
maxRes = []

def dfs(points, k):
    global res
    global digit
    global maxRes
    # print(res)
    # print(k)
    if k == len(points):
        return
    if digit[k] == -1:
        if len(res) == 0:
            res.append(k)
            # print("k" + str(k))
            if len(res) > len(maxRes):
                maxRes = res.copy()
            dfs(points, k + 1)
            del res[-1]
            # print("k")
            # print(res)
            dfs(points, k + 1)
        else:
            if points[res[-1]].y <= points[k].x:
                res.append(k)
                if len(res) > len(maxRes):
                    maxRes = res.copy()
                dfs(points, k + 1)
                del res[-1]

            dfs(points, k + 1)


for i in range(t):
    n = int(input())
    arr = input()
    x = [int(k) for k in arr.split(" ")]
    arr = input()
    y = [int(k) for k in arr.split(" ")]
    points = []
    for k in range(n):
        points.append(Point(x[k], y[k], k + 1))
    points.sort(key=lambda p: p.x)
    res = []
    digit = [-1 for i in range(10000)]
    maxRes = []
    dfs(points, 0)
    for j in range(len(maxRes)):
        if j == len(maxRes) - 1:
            print(points[maxRes[j]].index)
        else:
            print(points[maxRes[j]].index, end=" ")
