def checkwin():
    index = -1
    for i in range(3):
        if (board[i][0]==board[i][1] and board[i][1]==board[i][2])or(board[0][i]==board[1][i] and board[1][i]==board[2][i]):
            if(board[i][i]==0):
                index=1
            elif(board[i][i]==1):
                index=2
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        if(board[1][1]==0):
           index=1
        elif(board[1][1]==1):
           index=2
    return index

if __name__ == '__main__':
    lists = list(eval(input()))
    board=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    index=-1
#由于不易面向对象，将index分为正在进行-1，平局0，a赢1，b赢2
    for i in range(len(lists)):
        a=lists[i][0]
        b=lists[i][1]
        if i%2==0:
            board[a][b]=0
        else:
            board[a][b]=1
        index = checkwin()
        if i==len(lists)-1 and index==-1 and len(lists)==9:
            index=0
        if index>=0:
           break
    if index==-1:
        print("Pending")
    elif index==0:
        print("Draw")
 #       print(lists)
    elif index==1:
        print("A")
    elif index==2:
        print("B")