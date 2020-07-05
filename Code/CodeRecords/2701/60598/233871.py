moves = input()[1:-1]
i = 1
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def check(row,col):
    crow = row
    ccol = col
    symbol = board[crow][ccol]
    if board[crow][0] == board[crow][1] == board[crow][2]:
        return True
    if board[0][ccol] == board[1][ccol] == board[2][ccol]:
        return True
    if board[0][0] == board[1][1] == board[2][2] == board[crow][ccol]:
        return True
    if board[0][2] == board[1][1] == board[2][0] == board[crow][ccol]:
        return True
    return False
def full():
    for j in range(3):
        for k in range(3):
            if board[j][k] == " ":
                return False
    return True


finish = False
sign = "X"
player = "A"
while i < len(moves):
    row = int(moves[i:i+1])
    col = int(moves[i+2:i+3])
    board[row][col] = sign
    if check(row, col):
        print(player)
        finish = True
        break
    if player == "A":
        player = "B"
        sign = "O"
    else:
        player = "A"
        sign = "X"
    i += 6

if not finish:
    if full():
        print("Draw")   
    else:
        print("Pending")
