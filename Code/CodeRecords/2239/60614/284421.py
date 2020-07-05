board=input().split(',')
countX=0
countY=0
for i in range(3):
    countX+=board[i].count('X')
    countY+=board[i].count('O')
if countX==countY or countX==countY+1:
    countWin=board.count('XXX')+board.count('OOO')
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=" ":
            countWin+=1
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=" ":
        countWin+=1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!=" ":
        countWin += 1
    if countWin>1:
        print(False)
    else:
        print(True)
else:
    print(False)