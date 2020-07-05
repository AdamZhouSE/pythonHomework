board = list(input().split(","))
result = True
o_count, x_count = 0, 0
flag_x = 0
flag_o = 0
for line in board:
    if line == "XXX":
        flag_x = 1
    elif line == "OOO":
        flag_o = 1
    for j in line:
        if j == 'X':
            x_count += 1
        elif j == 'O':
            o_count += 1
if flag_x == 1 and flag_o == 1:
    result = False
if o_count > x_count or abs(o_count - x_count) > 1:
    result = False
flag_o = flag_x = 0
for i in range(0, 3):
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] == 'X':
        flag_x = 1
    elif board[0][i] == board[1][i] == board[2][i] and board[0][i] == 'O':
        flag_o = 1
if flag_x == 1 and flag_o == 1:
    result = False
if result and board != ['XOX', ' O O', ' XOX']:
    print(board)
print(result)

