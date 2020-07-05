def boundedRobot(instructions):
    x, y = 0, 0
    direction = 0
    increment = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(len(instructions)):
        if instructions[i] == 'L':
            direction -= 1
        elif instructions[i] == 'R':
            direction += 1
        else:
            direction %= 4
            x += increment[direction][0]
            y += increment[direction][1]
    return direction % 4 != 0 or (x == 0 and y == 0)

instructions = input()
print(boundedRobot(instructions))