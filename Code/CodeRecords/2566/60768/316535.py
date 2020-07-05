n = int(input())
room = []
for i in range(n):
    room.append(eval(input()))
re = []


def move(i, j, current, min_k):
    if current < min_k:
        min_k = current
    if i == len(room) - 1 and j == len(room[0]) - 1:
        current += room[i][j]
        if current < min_k:
            min_k = current
        re.append(min_k)
    elif i == len(room) - 1:
        move(i, j + 1, current + room[i][j], min_k)
    elif j == len(room[0]) - 1:
        move(i + 1, j, current + room[i][j], min_k)
    else:
        move(i, j + 1, current + room[i][j], min_k)
        move(i + 1, j, current + room[i][j], min_k)


move(0, 0, 0, 0)
print(1 - max(re))