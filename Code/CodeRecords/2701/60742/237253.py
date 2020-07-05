import re
str = input()
steps = []
for i in range(len(str)):
    if re.match('[0-9]',str[i]):
        steps.append(str[i])
len = len(steps)//2
moves = []
for i in range(len):
    moves.append([int(steps[2*i]),int(steps[2*i+1])])
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(len):
    if i%2==0:
        board[moves[i][0]][moves[i][1]] = "A"
    else:
        board[moves[i][0]][moves[i][1]] = "B"
if (board[0][0]!=" ") and ((board[0][0]==board[1][1] and board[1][1]==board[2][2])
or (board[0][0]==board[0][1] and board[0][1]==board[0][2])
or (board[0][0]==board[1][0] and board[1][0]==board[2][0])):
    res = board[0][0]
elif (board[1][1]!=" ") and ((board[1][1]==board[0][1] and board[1][1]==board[2][1])
or (board[1][1]==board[1][0] and board[1][1]==board[1][2])
or (board[1][1]==board[0][2] and board[1][1]==board[2][0])):
    res = board[1][1]
elif (board[2][2]!=" ") and ((board[2][2]==board[2][0] and board[2][2]==board[2][1])
or (board[2][2]==board[0][2] and board[2][2]==board[1][2])):
    res = board[2][2]
else:
    res = "Draw"
    for j in board:
        if " " in j:
            res = "Pending"
            break
print (res)