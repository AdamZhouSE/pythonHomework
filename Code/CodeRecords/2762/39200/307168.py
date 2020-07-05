from math import sqrt


def checkdir(d):
    if d > 3:
        d -= 4
    elif d < 0 :
        d += 4
    return d


t = int(input())
for x in range(t):
    m = int(input())
    string = input().split()
    moves = []
    i = 0
    while i < len(string):
        moves.append([string[i], int(string[i+1])])
        i += 2
    x = 0
    y = 0
    directions = ["N","W","S","E"]
    nowd = 0
    for move in moves:
        if move[0] == "U":
            if nowd == 0:
                y += move[1]
            elif nowd == 1:
                x -= move[1]
            elif nowd == 2:
                y -= move[1]
            elif nowd == 3:
                x += move[1]
        elif move[0] == "D":
            nowd += 2
            nowd = checkdir(nowd)
            if nowd == 0:
                y += move[1]
            elif nowd == 1:
                x -= move[1]
            elif nowd == 2:
                y -= move[1]
            elif nowd == 3:
                x += move[1]
        elif move[0] == "L":
            nowd += 1
            nowd = checkdir(nowd)
            if nowd == 0:
                y += move[1]
            elif nowd == 1:
                x -= move[1]
            elif nowd == 2:
                y -= move[1]
            elif nowd == 3:
                x += move[1]
        elif move[0] == "R":
            nowd -= 1
            nowd = checkdir(nowd)
            if nowd == 0:
                y += move[1]
            elif nowd == 1:
                x -= move[1]
            elif nowd == 2:
                y -= move[1]
            elif nowd == 3:
                x += move[1]
    print(int(sqrt(x**2+y**2)), directions[nowd])
