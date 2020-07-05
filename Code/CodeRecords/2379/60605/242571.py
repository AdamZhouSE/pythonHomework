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

print(isRobotBounded(input().strip()))
