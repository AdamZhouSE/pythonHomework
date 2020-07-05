def isValid(board):
    cnt = 0
    for x in range(3):
        if(board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] != ' '):
            cnt += 1
        if(board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] != ' '):
            cnt += 1
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' '):
        cnt += 1
    elif(board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != ' '):
        cnt += 1
    if(cnt > 1):
        return False
    else:
        return True

def count(board):
    X = 0
    O = 0
    for x in range(3):
        for y in range(3):
            if(board[x][y] == 'X'):
                X += 1
            elif(board[x][y] == 'O'):
                O += 1
    if(abs(X-O) > 1):
        return False
    else:
        if(O != 0 and X == 0):
            return False
        else:
            return True



temp = input().split(",")
board = []
for t in temp:
    board.append(list(t))
if(count(board) and isValid(board)):
    print(True)
else:
    print(False)