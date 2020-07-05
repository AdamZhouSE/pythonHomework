"""
分析表明，如果阻碍者直接到达目的地会阻碍我们，那么它无论怎么走都会阻碍我们
于是问题简化为：
我们与所有阻碍者都在最短时间内到达目的地是否会相遇

曼哈顿距离：网格中从A点到B点的距离，
公式为abs(x1-x2)+abs(y1-y2)
"""


def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


num_of_ghosts = int(input())
ghosts = []
for i in range(num_of_ghosts):
    inp = input().split(",")
    ghosts.append([int(inp[0]), int(inp[1])])
inp = input().split(",")
target = [int(inp[0]), int(inp[1])]
mine_dis = distance([0, 0], target)
for i in range(num_of_ghosts):
    if mine_dis >= distance(ghosts[i], target):
        print(False)
        exit()
print(True)
