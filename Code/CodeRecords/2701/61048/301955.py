def search9():
    set=[]
    str = list(input()[2 : - 2].split('],['))
    for i in range(len(str)):
        arr=[int(x) for x in str[i].split(',')]
        set.append(arr)
    board=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(set)):
        '''1 represents X and 2 O'''
        board[set[i][0]][set[i][1]]=1 if i % 2==0 else 2

    res=win(board)
    print(res)
    return


def win(board):
    over=False
    winner=0
    Draw=True
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                Draw=False
                break
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][2]==board[i][1] and board[i][0]!=0:
            over=True
            winner=board[i][0]
            break
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[0][i] != 0:
            over = True
            winner = board[0][i]
            break
        if board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[0][0]!=0:
            over = True
            winner = board[0][0]
            break
        if board[2][0] == board[1][1] and board[0][2] == board[1][1] and board[1][1] != 0:
            over=True
            winner=board[1][1]
            break
    if(Draw):
        return 'Draw'
    if(over):
        return 'A'if winner==1 else 'B'
    else:
        return 'Pending'

search9()