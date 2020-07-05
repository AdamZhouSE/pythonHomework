# 计算我们到目的地的曼哈顿距离是否小于所有阻碍者到达目的地的曼哈顿距离。
# 只要在终点能相遇，那么说明在中途一定能相遇


def escapeGhosts(ghosts, target) -> bool:
    return abs(target[0]) + abs(target[1]) < min([abs(target[0] - g[0]) + abs(target[1] - g[1]) for g in ghosts])

n = int(input())
ghosts = []
for i in range(n):
    ghosts.append([int(i) for i in input().split(",")])
target = [int(i) for i in input().split(",")]


print(escapeGhosts(ghosts,target))