board=input().split(',')
cntx=0
cnto=0
for i in range(0,3):
    for j in range(0,3):
        if board[i][j]=='X':
            cntx+=1
        elif board[i][j]=='O':
            cnto+=1
if not(cntx==cnto or cntx==cnto+1):
    print(False)
else:
    line=0
    for i in range(0,3):
        if board[i][0]!=' ' and board[i][1]==board[i][0] and board[i][2]==board[i][0]:
            line+=1
        if board[0][i]!=' ' and board[1][i]==board[0][i] and board[2][i]==board[0][i]:
            line+=1
    if board[1][1]!=' ' and board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        line+=1
    if board[1][1]!=' ' and board[0][2]==board[1][1] and board[2][0]==board[1][1]:
        line+=1
    if line>1:
        print(False)
    else:
        print(True)
            