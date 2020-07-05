import math

n = int(input())
for i in range(0, n):
    length = int(input())
    moves = input().split(" ")

    # 获取完输入，开始处理数据
    face = "North"
    x = 0
    y = 0
    for j in range(0, length):
        direction = moves[2*j]
        distance = int(moves[2*j+1])
        if face == "North":
            if direction == 'U':
                y += distance
            elif direction == 'D':
                y -= distance
                face = "South"
            elif direction == 'R':
                x += distance
                face = "East"
            else:
                x -= distance
                face = "West"
        elif face == "South":
            if direction == 'U':
                y -= distance
            elif direction == 'D':
                y += distance
                face = 'North'
            elif direction == 'R':
                x -= distance
                face = "West"
            else:
                x += distance
                face = "East"
        elif face == "East":
            if direction == 'U':
                x += distance
            elif direction == 'D':
                x -= distance
                face = "West"
            elif direction == 'L':
                y += distance
                face = "North"
            else:
                y -= distance
                face = "South"
        else:
            if direction == 'U':
                x -= distance
            elif distance == 'D':
                x += distance
                face = "East"
            elif distance == 'L':
                y -= distance
                face = "South"
            else:
                y += distance
                face = "North"
    d = int(math.sqrt(x**2 + y**2))
    print(d, end=" ")
    print(face[0])

