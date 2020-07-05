def possibleBoard(board):
    X_count = 0
    O_count = 0
    for row in board:
        for c in row:
            if c == 'X':
                X_count += 1
            if c == 'O':
                O_count += 1
    if X_count - O_count != 0 and X_count - O_count != 1:
        return 'False'

    res = []
    for i in range(3):
        res.append(board[i])  # 行
        s = ""
        for j in range(3):
            s += board[j][i]  # 列
        res.append(s)
    if 'XXX' in res and 'OOO' in res:
        return 'False'

    return 'True'

board = input().split(',')
print(possibleBoard(board))