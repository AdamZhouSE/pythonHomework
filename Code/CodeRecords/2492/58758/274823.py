C, N = [int(x) for x in input().split()]
grassland = []  # 草场坐标
for i in range(N):
    x, y = [int(x) for x in input().split()]
    grassland.append([max(x, y), min(x, y)])  # 把大的坐标存在前面，方便排序
grassland.sort()
print(grassland[C-1][0])  # 直接输出第C远的草场有多远即可
