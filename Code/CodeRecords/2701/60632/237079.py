def judge(xboard):
    if xboard[0][0] == xboard[1][1] == xboard[2][2]:  # 主对角线
        return board[1][1]
    if xboard[0][2] == xboard[1][1] == xboard[2][0]:  # 副对角线
        return board[1][1]
    for j in range(3):
        if xboard[j][0] == xboard[j][1] == xboard[j][2] == 'A'\
                or xboard[j][0] == xboard[j][1] == xboard[j][2] == 'B':  # 行
            return xboard[j][1]
    for j in range(3):
        if xboard[0][j] == xboard[1][j] == xboard[2][j] == 'A'\
                or xboard[0][j] == xboard[1][j] == xboard[2][j] == 'B':  # 列
            return xboard[1][j]
    if xboard[0].count('-') + xboard[1].count('-') + xboard[2].count('-') == 0:
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
