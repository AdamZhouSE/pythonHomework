board = list(input().split(","))
result = True
o_count, x_count = 0, 0
for line in board:
    if line == "XXX" or "OOO":
        result = False
    for j in line:
        if j == 'X':
            x_count += 1
        elif j == 'O':
            o_count += 1
if o_count > x_count or abs(o_count - x_count > 1):
    result = False
for i in range(0, 3):
    if board[0][i] == board[1][i] == board[2][i] != ' ':
        result = False
if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
    result = False
print(result)