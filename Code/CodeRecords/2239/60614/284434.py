board=input().split(',')
countX=0
countY=0
for i in range(3):
    countX+=board[i].count('X')
    countY+=board[i].count('O')
if countX==countY or countX==countY+1:
    Win=' '
    if 'XXX' in board:
        Win='X'
    if 'OOO' in board:
        if Win=='X':
            Win='W'#Wrong
    if Win!='W':
        for i in range(3):
            if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=" ":
                if board[0][i]!=Win:
                    Win='W'
                    break
    if Win!='W':
        if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=" ":
            if board[0][0] != Win:
                Win = 'W'
    if Win != 'W':
        if board[0][2] == board[1][1] == board[2][0] and board[0][2]!=" ":
            if board[0][2] != Win:
                Win = 'W'
    if Win=='W':
        print(False)
    else:
        print(True)
else:
    print(False)