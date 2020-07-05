line = int(input())
board = []
for i in range(line):
    board.append(list(input()))
x = 0
for i in range(line):
    for j in range(line):
        o_num = 0
        if i != 0:
            if board[i-1][j] == "o":
                o_num = o_num + 1
        if j != 0:
            if board[i][j-1] == "o":
                o_num = o_num + 1
        if i != line-1:
            if board[i+1][j] == "o":
                o_num = o_num + 1
        if j != line-1:
            if board[i][j+1] == "o":
                o_num = o_num + 1
        if o_num % 2 != 0:       
            x = 1
if x == 1:
    print("NO")
else:
    print("YES")