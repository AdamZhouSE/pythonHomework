situation=[[] for i in range(3)]
for i in range(3):
    for j in range(3):
        situation[i].append(0)
string=input()
i=2
moves=[]
while i<len(string):
    moves.append(string[i:i+3])
    i+=6
for i in range(len(moves)):
    move=moves[i]
    line=int(move[0:1])
    column=int(move[2:3])
    if i%2==0:
        situation[line][column]="X"
    else:
        situation[line][column]="O"
result=""
for i in range(3):
    if situation[i][0]=="X" and situation[i][1]=="X" and situation[i][2]=="X":
        result="A"
    elif situation[i][0]=="O" and situation[i][1]=="O" and situation[i][2]=="O":
        result="B"
for i in range(3):
    if situation[0][i]=="X" and situation[1][i]=="X" and situation[2][i]=="X":
        result="A"
    elif situation[0][i]=="O" and situation[1][i]=="O" and situation[2][i]=="O":
        result="B"
if situation[0][0] == "X" and situation[1][1] == "X" and situation[2][2] == "X":
    result = "A"
elif situation[0][0] == "O" and situation[1][1] == "O" and situation[2][2] == "O":
    result = "B"
if situation[2][0] == "X" and situation[1][1] == "X" and situation[0][2] == "X":
    result = "A"
elif situation[2][0] == "O" and situation[1][1] == "O" and situation[0][2] == "O":
    result = "B"
if result=="":
    p=0
    for i in range(3):
        for j in range(3):
            if situation[i][j]==0:
                p=1
    if p==1:
        result="Pending"
    else:
        result="Draw"
print(result)