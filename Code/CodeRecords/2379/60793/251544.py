instructions = list(input())
current_place = [0, 0]
direction = 1
for i in instructions:
    if i == 'L':
        direction -= 1
        if direction == 0:
            direction = 4
    elif i == 'R':
        direction = (direction + 1) % 4
    elif i == 'G':
        if direction == 1:
            current_place[1] += 1
        elif direction == 2:
            current_place[0] += 1
        elif direction == 3:
            current_place[1] -= 1
        elif direction == 4:
            current_place[0] -= 1
if current_place == [0, 0]:
    print("True")
else:
    print("False")
