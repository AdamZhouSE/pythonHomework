instructions=input()
x, y, dx, dy = 0, 0, 0, 1
for i in instructions:
    if i == 'R':
        dx, dy = dy, -dx
    elif i == 'L':
        dx, dy = -dy, dx
    elif i == 'G':
        x, y = x + dx, y + dy
print((x, y) == (0, 0) or (dx, dy) != (0, 1))