def makemove(letter, row, column, board):
    board[row][column] = letter


def judge(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        return board[2][0]
    else:
        return "N"



ori = input()
moves = []
for i in range(1, len(ori), 6):
    moves.append(ori[i:i+6])
moves.append(ori[len(ori)-6:len(ori)-1])
theBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
for i in range(len(moves)):
    if i % 2 == 0:
        makemove('X', int(moves[i][1]), int(moves[i][3]), theBoard)
    else:
        makemove('O', int(moves[i][1]), int(moves[i][3]), theBoard)
    l = judge(theBoard)
    if l != "N":
        if l == 'X':
            print("A")
        else:
            print("B")
        break
if judge(theBoard) == "N":
    if len(moves) < 9:
        print("Pending")
    else:
        print("Draw")
