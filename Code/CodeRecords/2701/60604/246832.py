a=input()
board=[]
a=a[1:len(a)-1].lstrip('[').rstrip(']').split('],[')
board.append(list("---"))
board.append(list("---"))
board.append(list("---"))


#print(board)
now='A'
for i in range(len(a)):
    x=int(a[i][0])
    y=int(a[i][2])
    #print(str(x)+" "+str(y))
    if now=='A':
        board[x][y]='A'
        #print(board[x+1])
        #print(board[x][y]+str(x)+str(y))
    else:
        board[x][y]='B'
    #print(board)
    if now =='A':
        now='B'
    else:
        now='A'
#print(board)
def winner(board):
    res="Draw"
    if board[0][0]==board[0][1] and board[0][0]==board[0][2] and board[0][0]!='-':
        res=board[0][0]
    elif board[1][0]==board[1][1] and board[1][0]==board[1][2]and board[1][0]!='-':
        res=board[1][0]
    elif board[2][0]==board[2][1] and board[2][0]==board[2][2]and board[2][2]!='-':
        res=board[2][0]
    elif board[0][0]==board[1][0] and board[1][0]==board[2][0]and board[0][0]!='-':
        res=board[1][0]
    elif board[1][1]==board[0][1] and board[1][1]==board[2][1]and board[0][1]!='-':
        res=board[1][1]
    elif board[0][2]==board[1][2] and board[1][2]==board[2][2]and board[0][2]!='-':
        res=board[1][2]
    elif board[0][0]==board[1][1] and board[1][1]==board[2][2]and board[0][0]!='-':
        res=board[1][1]
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2]and board[0][2]!='-':
        res=board[1][1]
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j]=='-':
                    return "Pending"
    return res
print(winner(board))
    
    