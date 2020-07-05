def win(lst,c):
    win=0
    for i in range(3):
        if lst[0][i]==c and lst[1][i]==c and lst[2][i]==c:
            win+=1
        if lst[i][0]==c and lst[i][1]==c and lst[i][2]==c:
            win+=1
    if lst[0][0]==c and lst[1][1]==c and lst[2][2]==c:
        win+=1
    if lst[0][2]==c and lst[1][1]==c and lst[2][0]==c:
        win+=1
    return win

inp=input().split(",")
board=[]
for i in range(3):
    board.append(list(inp[i]))
xnum=0
onum=0
res="True"
for m in range(3):
    for k in board[m]:
        if k == 'X':
            xnum += 1
        if k == 'O':
            onum += 1
if(xnum-onum>1 or onum-xnum>0):
    res = 'False'
if(xnum!=onum and xnum!=onum+1):
    res='False'
if(win(board,'X')>1 or win(board,'O')>1):
    res='False'
if(win(board,'X')==1 and win(board,'O')==1) :
    res = 'False'
if(win(board,'X')==1 and xnum!=onum+1):
    res = 'False'
if(win(board,'O')==1 and xnum!=onum):
    res='False'
# if (win(board,'X')==1 and xnum==onum+1):
#     res="True"
# if(win(board,'O')==1 and xnum==onum):
#     res = "True"
# if(win(board,'O')==0 and win(board,'X')==0 and (xnum==onum+1 or xnum==onum)):
#     res = "True"
print(res)