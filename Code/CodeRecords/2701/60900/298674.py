table =[[" "," "," "],[" "," "," "],[" "," "," "]]
str0 = input()
moves =[]
for i in range(0,len(str0)):
    if str0[i]!='[' and str0[i]!=']' and str0[i]!=',':
        moves.append(int(str0[i]))
for i in range(0,int((len(moves))/2)):
    a = moves[2*i]
    b = moves[2*i+1]
    if i%2==0:
        table[a][b] = "X"
    else:
        table[a][b] = "O"
result =" "
if table[0][0] == table[0][1] == table[0][2]:
    if table[0][0] == "X":result ="A"
    if table[0][0] == "O": result ="B"
if table[1][0] == table[1][1] == table[1][2]:
    if table[1][0] == "X":result ="A"
    if table[1][0] == "O": result ="B"
if table[2][0] == table[2][1] == table[2][2]:
    if table[2][0] == "X":result ="A"
    if table[2][0] == "O": result ="B"
if table[0][0] == table[1][0] == table[2][0]:
    if table[0][0] == "X":result ="A"
    if table[0][0] == "O": result ="B"
if table[0][1] == table[1][1] == table[2][1]:
    if table[0][1] == "X":result ="A"
    if table[0][1] == "O": result ="B"
if table[0][2] == table[1][2] == table[2][2]:
    if table[0][2] == "X":result ="A"
    if table[0][2] == "O": result ="B"
if table[0][0] == table[1][1]  ==table[2][2]:
    if table[0][0] == "X":result ="A"
    if table[0][0] == "O": result ="B"
if table[2][0] == table[1][1] == table[0][2]:
    if table[2][0] == "X":result ="A"
    if table[2][0] == "O": result ="B"
if result==" ":
    if " " in table[0] or " " in table[1] or " " in table[2]:
        result ="Pending"
    else:
        result ="Draw"
print(result)