def isWin(board):
    for x in range(3):
        if(board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] != ' '):
            return 'A' if(board[x][0] == 'X') else 'B'
        elif(board[0][x] == board[1][x] and board[1][x] == board[2][x] == board[0][x] != ' '):
            return 'A' if(board[0][x] == 'X') else 'B'
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' '):
        return 'A' if(board[0][0] == 'X') else 'B'
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' '):
        return 'A' if(board[1][1] == 'X') else 'B'
    return None

ways = []
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
nums = input()[2:-2].split("],[")
for num in nums:
    num = list(map(int,num.split(",")))
    ways.append(num)

now = 'X'
for way in ways:
    board[way[0]][way[1]] = now
    now = 'Y' if(now == 'X') else 'X'
    situation = isWin(board)
    if(situation!=None):
        print(situation)
        break
if(situation == None):
    if(len(ways) < 9):
        print("Pending")
    else:
        print("Draw")