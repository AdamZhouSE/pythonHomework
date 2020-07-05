import re
step=list(map(int,re.sub("\D"," ",input()).split()))
storia=[["-1"]*3 for i in range(3)]
chess="A"
winner="-1"
for j in range(0,len(step)-1,2):
    storia[step[j]][step[j+1]]=chess
    if chess=="A":
        chess="B"
    else:
        chess="A"
for k in range(3):
    if storia[k][0]==storia[k][1] and storia[k][1]==storia[k][2] and storia[k][0]!="-1":
        winner=storia[k][0]
        break
    if storia[0][k]==storia[1][k] and storia[1][k]==storia[2][k] and storia[k][0]!="-1":
        winner=storia[0][k]
        break
if storia[0][0]==storia[1][1] and storia[1][1]==storia[2][2] and storia[1][1]!="-1":
    winner=storia[1][1]
if storia[0][2]==storia[1][1] and storia[1][1]==storia[2][0] and storia[1][1]!="-1":
    winner=storia[1][1]
if winner=="-1":
    if len(step)==18:
        winner="Draw"
    else:
        winner="Pending"
print(winner)