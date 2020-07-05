moves = eval(input())
res = [[0,0,0],[0,0,0],[0,0,0]]
ml = len(moves)
win = 0
for i in range(0,ml):
    if i%2 == 0:
        res[moves[i][0]][moves[i][1]] = 1
    else:
        res[moves[i][0]][moves[i][1]] = 2
    if res[0][0]==res[0][1] and res[0][0] == res[0][2] and res[0][0] != 0:
        win = 1
        if res[0][0] == 1:
            print("A")
        else:
            print("B")
        break
    if res[1][0]==res[1][1] and res[1][0] == res[1][2] and res[1][0] != 0:
        win = 1
        if res[1][0] == 1:
            print("A")
        else:
            print("B")
        break
    if res[2][0]==res[2][1] and res[2][0] == res[2][2] and res[2][0] != 0:
        win = 1
        if res[2][0] == 1:
            print("A")
        else:
            print("B")
        break
    if res[0][0]==res[1][1] and res[0][0] == res[2][2] and res[0][0] != 0:
        win = 1
        if res[0][0] == 1:
            print("A")
        else:
            print("B")
        break
    if res[2][0]==res[1][1] and res[1][1] == res[0][2] and res[2][0] != 0:
        win = 1
        if res[1][1] == 1:
            print("A")
        else:
            print("B")
        break
    if res[0][0]==res[1][0] and res[0][0] == res[2][0] and res[0][0] != 0:
        win = 1
        if res[0][0] == 1:
            print("A")
        else:
            print("B")
        break
    if res[0][1]==res[1][1] and res[0][1] == res[2][1] and res[0][1] != 0:
        win = 1
        if res[0][0] == 1:
            print("A")
        else:
            print("B")
    if res[0][2]==res[1][2] and res[0][2] == res[2][2] and res[0][2] != 0:
        win = 1
        if res[0][0] == 1:
            print("A")
        else:
            print("B")
        break
if ml == 9 and not win:
    print("Draw")
elif ml < 9 and not win:
    print("Pending")