import math

def isfinish(l):
    for i in range(3):
        if (l[i][0] == l[i][1] and l[i][1] == l[i][2]) or (l[0][i] == l[1][i] and l[1][i] == l[2][i]):
            return True
        elif (l[0][0] == l[1][1] and l[1][1] == l[2][2]) or (l[2][0] == l[1][1] and l[1][1] == l[0][2]):
            return True
        else:
            return False


def countchar(c, l):
    count = 0
    for i in range(3):
        for j in range(3):
            if l[i][j] == c:
                count += 1
    return count


l = input().split(',')

countX = countchar('X', l)
countO = countchar('O', l)

if countO == 1 and countX == 0:
    print(False)
else:
    if int(math.fabs(countO - countX)) > 1:
        print(False)
    else:
        if isfinish(l):
            print(False)
        else:
            print(True)

#"XOX", "O O", "XOX"