def judge(board):
    if board[0][0] == board[1][1] == board[2][2]:  # 主对角线
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0]:  # 副对角线
        return board[1][1]
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2]:  # 行
            return board[j][1]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:  # 列
            return board[1][j]
    if board[0].count('-') + board[1].count('-') + board[2].count('-') == 0:
        return 'Draw'
    else:
        return 'Pending'


get = input()[1:-1]
moves = []
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
for i in range(0, len(get) - 4, 6):
    moves.append(list(map(int, (get[i:i+5])[1::2])))
for i in range(len(moves)):
    if i % 2 == 0:
        board[moves[i][0]][moves[i][1]] = 'A'
    else:
        board[moves[i][0]][moves[i][1]] = 'B'
# print(board[0])
# print(board[1])
# print(board[2])
print(judge(board))
