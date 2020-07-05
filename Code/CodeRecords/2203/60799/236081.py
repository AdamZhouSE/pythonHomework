import re


def isWin(box):
    for i in range(0, 3):
        win = True
        for j in range(0, 3):
            if box[i][j] != box[i][0]:
                win = False
        if win:
            return box[i][0]

    for j in range(0, 3):
        win = True
        for i in range(0, 3):
            if box[i][j] != box[0][j]:
                win = False
        if win:
            return box[0][j]

    if box[1][1] == box[0][0] == box[2][2] or box[1][1] == box[2][0] == box[0][2]:
        return box[1][1]

    for i in range(0, 3):
        for j in range(0, 3):
            if box[i][j] != 'A' and box[i][j] != 'B':  # and ，不是or
                return 'Pending'

    return 'Draw'


a = re.split('],\[|,', input().strip('[|]'))
a = [int(i) for i in a]
box = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
for i in range(0, len(a) - 1):
    if i % 2 == 0:
        if i % 4 == 0:
            box[a[i]][a[i + 1]] = 'A'
        else:
            box[a[i]][a[i + 1]] = 'B'
        aa = isWin(box)
        if aa != 'Pending':
            break

print(aa)
