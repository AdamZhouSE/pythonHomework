def judge():
    board = input().split(',')
    length = len(board)
    num_x = num_y = 0
    for i in board:
        for j in i:
            if j == 'X':
                num_x += 1
            elif j == 'O':
                num_y += 1
    if abs(num_y - num_x) >= 2:
        print(False)
        return

    win = 0
#     same in row
    for i in range(0, 3):
        if [0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            win += 1
#         same in col
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            win += 1
#         same in xie line
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        win += 1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        win += 1

    if win > 1:
        print(False)
        return 
    print(True)


judge()