def getWin(square):
    for i in range(0,3):
        if square[i][0] == square[i][1] == square[i][2] and square[i][0] != " ":
            if square[i][0] == "X":
                return "A"
            else:
                return "B"
        if square[0][i] == square[1][i] == square[2][i] and square[0][i] != " ":
            if square[i][0] == "X":
                return "A"
            else:
                return "B"
    if (square[0][0] == square[1][1] == square[2][2] or square[0][2] == square[1][1] == square[2][0]) and square [1][1] != " ":
        if square[1][1] == "X":
            return "A"
        else:
            return "B"
    return None


def judge():
    moves = eval(input())
    square = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for i in range(0, len(moves)):
        if i % 2 == 0:
            square[moves[i][0]][moves[i][1]] = "X"
        else:
            square[moves[i][0]][moves[i][1]] = "Y"
        s = getWin(square)
        if s is not None:
            print(s)
            return
    for i in range(0,3):
        for i in range(0,3):
            if square[i][j] == " ":
                print("Pending")
                return
    print("Draw")


judge()