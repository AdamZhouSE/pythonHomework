def move():
    i1=input().split('[')
    i1=''.join(i1).split(']')
    i1=''.join(i1).split(',')
    return i1

def check_raw(board):
    pending=True
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]!='':
            print(board[i][0])
            pending=False
    return pending

def check_line(board):
    pending=True
    for i in range(0,3):
        if board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]!='':
            print(board[i][0])
            pending=False
    return pending

def check_cross(board):
    pending=True
    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!='':
        print(board[0][0])
        pending=False
    if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!='':
        print(board[2][0])
        pending=False
    return pending

def check_draw(board):
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=='':
                return False
    return True

board=[['','',''],['','',''],['','','']]
turn=0
player=''
mv=list(map(int,move()))
for m in range(0,int(len(mv)/2)):
    if turn%2==0:
        player='A'
    else:
        player='B'
    board[mv[turn*2]][mv[turn*2+1]]=player
    turn=turn+1
if check_raw(board) and check_line(board) and check_cross(board):
    if check_draw(board):
        print('Draw')
    else:
        print('Pending')
        
        


            
        