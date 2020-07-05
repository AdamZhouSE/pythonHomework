moves = eval(input())
board = [[None,None,None] for i in range(3)]
for idx,move in enumerate(moves):
    if idx % 2 == 0:
        board[move[0]][move[1]] = 'A'
    else:
        board[move[0]][move[1]] = 'B'

def check(board:list):
    #横
    for i in range(3):
        if board[i][0] is not None and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
    #竖
    for i in range(3):
        if board[0][i] is not None and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    #斜
    if board[0][0] is not None and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] is not None and board[0][2] == board[1][1] and board[2][0] == board[0][2]:
        return board[0][2]

    #没人赢
    return None

result = check(board)
if result is not None:
    print(result)
else:
    if len(moves) == 9:
        print("Draw")
    else:
        print("Pending")