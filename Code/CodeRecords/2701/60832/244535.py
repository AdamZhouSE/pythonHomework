import sys

get = input()
if len(get) == 0:
    print("Pending")
    sys.exit()
ar = get[2:-2].split("],[")
tic = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, len(ar)):
    if i % 2 == 0:
        x = 1
    else:
        x = 2
    r = int(ar[i][0])
    c = int(ar[i][2])
    if tic[r][c] == 0:
        tic[r][c] = x
    else:
        print("bug")
        sys.exit()

    if (tic[0][0] == tic[0][1] and tic[0][2] == tic[0][1] and tic[0][0] > 0) or (
            tic[1][0] == tic[1][1] and tic[1][2] == tic[1][1] and tic[1][0] > 0) or (
            tic[2][0] == tic[2][1] and tic[2][2] == tic[2][1] and tic[2][0] > 0):
        if x == 1:
            print("A")
            sys.exit()
        else:
            print("B")
            sys.exit()

    if (tic[0][0] == tic[1][1] and tic[2][2] == tic[1][1] and tic[0][0] > 0) or (
            tic[0][2] == tic[1][1] and tic[2][0] == tic[1][1] and tic[2][0] > 0):
        if x == 1:
            print("A")
            sys.exit()
        else:
            print("B")
            sys.exit()

    if (tic[0][0] == tic[1][0] and tic[2][0] == tic[1][0] and tic[0][0] > 0) or (
            tic[0][1] == tic[1][1] and tic[2][1] == tic[1][1] and tic[0][1] > 0) or (
            tic[0][2] == tic[1][2] and tic[2][2] == tic[1][2] and tic[0][2] > 0):
        if x == 1:
            print("A")
            sys.exit()
        else:
            print("B")
            sys.exit()

if len(ar) == 9:
    print("Draw")
else:
    print("Pending")