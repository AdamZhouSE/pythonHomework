str=input()[2:-2]
list=str.split("],[")

for i in range(len(list)):
    list[i]=list[i].split(",")
    list[i][0]=int(list[i][0])
    list[i][1]=int(list[i][1])
board=[]
for i in range(3):
    row=[" "," "," "]
    board.append(row)
for i in range(len(list)):
    if i%2==0: board[list[i][0]][list[i][1]]="X"
    else:  board[list[i][0]][list[i][1]]="O"

winner=""
for i in range(3):
    if board[i][0]==board[i][1]==board[i][2]:
        if board[i][0]=="X": winner="A"
        else: winner="B"
        break
for i in range(3):
    if board[0][i]==board[1][i]==board[2][i]:
        if board[0][i]=="X":winner="A"
        else: winner="B"
        break
if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
    if board[1][1]=="X":winner="A"
    else:winner="B"
if winner=="":winner="Draw"
Ono,Xno=0,0
for i in range(3):
    for j in range(3):
        if board[i][j]=="O": Ono+=1
        elif board[i][j]=="X": Xno+=1
        else: continue
if Ono<3 and Xno<3: winner="Pending"
print(winner)