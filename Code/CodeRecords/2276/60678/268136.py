r = int(input())
c = int(input())
positionY = int(input())
positionX = int(input())
stepLines = [[positionY, positionX]]
directions = {0, 1, 2, 3, 4}
# 1 east ,  2 south,  3 west,  4 north
direction = 1
step = 1
count = 1
while count < r * c:
    for i in range(0, step):
        if direction == 1:
            positionX += 1
        elif direction == 2:
            positionY += 1
        elif direction == 3:
            positionX -= 1
        elif direction == 4:
            positionY -= 1
        if 0 <= positionX and positionX <= c - 1 and 0 <= positionY and positionY <= r - 1 and stepLines.count([positionY, positionX]) == 0:
            count += 1
            stepLines.append([positionY, positionX])


    if direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 4
    elif direction == 4:
        direction = 1

    for i in range(0, step):
        if direction == 1:
            positionX += 1
        elif direction == 2:
            positionY += 1
        elif direction == 3:
            positionX -= 1
        elif direction == 4:
            positionY -= 1
        if 0 <= positionX and positionX <= c - 1 and 0 <= positionY and positionY <= r - 1 and stepLines.count([positionY, positionX]) == 0:
            count += 1
            stepLines.append([positionY, positionX])

    if direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 4
    elif direction == 4:
        direction = 1


    step += 1
print(stepLines)