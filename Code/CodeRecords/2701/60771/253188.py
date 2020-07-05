#35
def judge(cells):
    winchar = ""
    for i in range(0,3):
        for j in range(0,1):
            if cells[i][j] != "_" and cells[i][j] == cells[i][j+1] and cells[i][j+1] == cells[i][j+2]:
                winchar = cells[i][j]
                break
    # 判断横着胜利
    if winchar == "":
        for j in range(0, 3):
            for i in range(0, 1):
                if cells[i][j] != "_" and cells[i][j] == cells[i + 1][j] and cells[i + 1][j] == cells[i + 2][j]:
                    winchar = cells[i][j]
                    break
    # 判断竖着胜利
    if winchar == "":
        # print(cells[0][0], cells[1][1], cells[2][2])
        # print(cells[0][0]==cells[1][1])
        # print(cells[1][1]==cells[2][2])
        # print(cells[0][0]==cells[1][1] and cells[1][1]==cells[2][2])
        if cells[0][0] == cells[1][1] and cells[1][1] == cells[2][2]:
            winchar = cells[0][0]
        if cells[2][0] == cells[1][1] and cells[1][1] == cells[0][2]:
            winchar = cells[2][0]
    # 判断斜着胜利
    if winchar == "A":
        print("A")
        return
    elif winchar == "B":
        print("B")
        return

    for i in range(0,3):
        for j in range(0,3):
            if cells[i][j] == "_":
                print("Pending")
                return

    print("Draw")
ori = input()
ori = ori[1:len(ori)-1] #去掉两头[]
oriList = ori.split("],")
moves = [] #初始化二维数组应该是把list加到list中..
for item in oriList:
    sub = []
    sub.append(int(item[1]))
    sub.append(int(item[3]))
    moves.append(sub)
cells = []
for i in range(0,3): #初始化棋盘
    row = ["_","_","_"]
    cells.append(row)
for i in range(0,len(moves)):# 布置棋盘
    x = moves[i][0]
    y = moves[i][1]
    if i%2 == 0 and cells[x][y] == "_":
        cells[x][y] = "A"
        # print("A: ",x,y)
    elif i%2 == 1 and cells[x][y] == "_":
        cells[x][y] = "B"
        # print("B: ", x, y)
# print(cells)
judge(cells)


