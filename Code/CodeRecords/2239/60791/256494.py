board = input().split(',')
count_X = 0
count_O = 0
for x in range(3):
    for y in range(3):
        if(board[x][y]=='X'):
            count_X += 1
        elif(board[x][y] == 'O'):
            count_O += 1
if(count_O > count_X or count_X-count_O > 1):
    print(False)
else:
    count = 0
    for i in range(3):
        if(board[i] == 'XXX' or board[i] == 'OOO'):
            count += 1
    for x in range(3):
        if((board[0][x]==board[1][x] and board[2][x]==board[1][x]) and (board[0][x]=='X'or board[0][x]=='O')):
            count += 1
    if((board[0][0]==board[1][1] and board[2][2]==board[1][1])and(board[0][0]=='X' or board[0][0]=='O')):
           count += 1
    if((board[2][0]==board[1][1] and board[0][2]==board[1][1])and(board[0][2]=='X' or board[0][2]=='O')):
           count += 1
    if(count >=2 or (count==1 and count_X == count_O)):
        print(False)
    else:
        print(True)