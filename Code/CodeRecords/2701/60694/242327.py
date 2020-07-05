moves = eval(input())
steps = len(moves)
chessBoard = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

for i in range(steps):
    row, column = moves[i][0], moves[i][1]
    if i % 2 == 0:
        chessBoard[row][column] = "X"
    else:
        chessBoard[row][column] = "O"

for i in range(3):
    if chessBoard[i].count("X") == 3 or chessBoard[0][i] + chessBoard[1][i] + chessBoard[2][i] == "XXX" \
            or chessBoard[0][0] + chessBoard[1][1] + chessBoard[2][2] == "XXX"\
            or chessBoard[0][2] + chessBoard[1][1] + chessBoard[2][0] == "XXX":
        print("A")
        exit()
    elif chessBoard[i].count("O") == 3 or chessBoard[0][i] + chessBoard[1][i] + chessBoard[2][i] == "OOO"\
            or chessBoard[0][0] + chessBoard[1][1] + chessBoard[2][2] == "OOO"\
            or chessBoard[0][2] + chessBoard[1][1] + chessBoard[2][0] == "OOO":
        print("B")
        exit()

for i in range(3):
    if " " in chessBoard[i]:
        print("Pending")
        exit()

print("Draw")

