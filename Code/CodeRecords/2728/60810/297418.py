'''
给定N个非负整数，其中每个代表坐标上的一个点（i，ai）。
绘制N条垂直线，使第i条线的两个端点位于（i，ai）和（i，0）。找到两条线，它们与x轴一起形成一个容器，以便该容器包含最多的水。
'''


def getMostWater(arr):
    res = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            tmp = min(int(arr[i]), int(arr[j])) * (j - i)
            if tmp > res:
                res = tmp
    print(res)


t = int(input())
for i in range(0, t):
    n = int(input())
    inp = input().split(' ')
    if inp[-1] == '':
        a = inp[0:len(inp) - 1]
    else:
        a = inp
    getMostWater(a)