moves = eval(input())

field = [[0 for i in range(3)] for i in range(3)]
next = 1
rest = 9

def printField():
    for row in field:
        print(' '.join(list(map(str, row))))
    print()

def testResult(x,y):
    if field[x][0] == field[x][1] == field[x][2] and field[x][0] != 0:
        return field[x][0]
    if field[0][y] == field[1][y] == field[2][y] and field[0][y] != 0:
        return field[0][y]
    if field[1][1] != 0 and (field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]):
        return field[1][1]
    return 0

mode = 'Pending'

for x,y in moves:
    field[x][y] = next
    if next == 2:
        next = 1
    else:
        next = 2
    rest -= 1
    # printField()

    result = testResult(x, y)
    if result != 0:
        mode = 'A' if result == 1 else 'B'
        break
    elif rest == 0:
        mode = 'Draw'
        break
print(mode)