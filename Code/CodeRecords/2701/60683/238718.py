nums = eval(input())
pan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def checkWin(x0, y0, cur0):
    if x0 == y0:
        j = 0
        while j < 3:
            if pan[j][j] != cur0:
                break
            j += 1
        if j == 3:
            return True
    if x0 + y0 == 2:
        j = 0
        while j < 3:
            if pan[j][2 - j] != cur0:
                break
            j += 1
        if j == 3:
            return True
    j = 0
    while j < 3:
        if pan[x0][j] != cur0:
            break
        j += 1
    if j == 3:
        return True
    j = 0
    while j < 3:
        if pan[j][y0] != cur0:
            break
        j += 1
    if j == 3:
        return True
    return False


flag = False
winner = ''
cur = 1
for i in range(len(nums)):
    x = nums[i][0]
    y = nums[i][1]
    pan[x][y] = cur
    if i >= 4:
        if checkWin(x, y, cur):
            flag = True
            winner = 'A' if cur == 1 else 'B'
            break
    cur = -cur

if flag:
    print(winner)
else:
    if len(nums) == 9:
        print('Draw')
    else:
        print('Pending')