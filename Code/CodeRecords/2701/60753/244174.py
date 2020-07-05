import sys
import re
import math
def checkboard(a,board):
    if board[0][0]==a and board[0][1]==a and board[0][2]==a:
        return 1
    elif board[0][0]==a and board[1][0]==a and board[2][0]==a:
        return 1
    elif board[1][0]==a and board[1][1]==a and board[1][2]==a:
        return 1
    elif board[2][0]==a and board[2][1]==a and board[2][2]==a:
        return 1
    elif board[0][1]==a and board[1][1]==a and board[2][1]==a:
        return 1
    elif board[0][2]==a and board[1][2]==a and board[2][2]==a:
        return 1
    elif board[0][0]==a and board[1][1]==a and board[2][2]==a:
        return 1
    elif board[2][0]==a and board[1][1]==a and board[0][2]==a:
        return 1
    else:
        return 0
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
board = [[0]*3 for i in range(3)]
awin=0
bwin=0
for i in range(len(listline)/2):
    if i%2==0:
        board[listline[2*i]][listline[2*i+1]]=1
        awin=checkboard(1,board)
        if awin==1:
            break
    else:
        board[listline[2*i]][listline[2*i+1]]=2
        bwin=checkboard(2,board)
        if bwin==1:
            break
if awin==1:
    print("A")
elif bwin==1:
    print("B")
else:
    full=1
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                full=0
                break
    if full==0:
        print("Draw")
    else:
        print("Pending")

