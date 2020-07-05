#需要对指令序列做重复，那么最多重复4次必然可以回到起点（如果可以的话）。
# 为什么呢？因为我们最少可以转90度（在保证可以回到原点的情况下）。
def isRobotBounded(instructions: str) -> bool:
    x, y, dx, dy = 0, 0, 0, 1
    instructions *= 4
    for i in instructions:
        if i == 'R':
            dx, dy = dy, -dx
        elif i == 'L':
            dx, dy = -dy, dx
        elif i == 'G':
            x, y = x + dx, y + dy
    return (x, y) == (0, 0)
print(isRobotBounded(input()))
