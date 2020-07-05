board=[[" "," "," "],[" "," "," "],[" "," "," "],]
a=list(input())
while "[" in a:
    a.remove("[")
while "]" in a:
    a.remove("]")
while "," in a:
    a.remove(",")
step=[]
for i in range(0,len(a),2):
    step.append([int(a[i]),int(a[i+1])])
for i in range(0,len(step)):
    if i%2==0:
        board[step[i][0]][step[i][1]]="X"
    else:
        board[step[i][0]][step[i][1]]="O"
    flag=False
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][0]==board[i][2]:
            flag=True
            if board[i][0]=="X":
                winner="A"
            else:
                winner="B"
        if board[0][i]==board[1][i] and board[0][i]==board[2][i]:
            flag=True
            if board[0][i]=="X":
                winner="A"
            else:
                winner="B"
    if (board[0][0]==board[1][1] and board[0][0]==board[2][2]) or (board[0][2]==board[1][1] and board[2][0]==board[1][1]):
        flag=True
        if board[1][1] == "X":
            winner="A"
        else:
            winner="B"
if flag:
    print(winner)
else:
    if len(step)==9:
        print("Draw")
    else:
        print("Pending")