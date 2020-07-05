s=input()
str=[]
chess=[ [" "] * 3 for i in range(3)]
result='Pending'
for item in s:
    if item>='0' and item<='2':
        str.append(int(item))
next='A'
for i in range(0,len(str)-1,2):
    m=str[i]
    n=str[i+1]
    if next=='A':
        chess[m][n]='X'
        next='B'
    else:
        chess[m][n]='O'
        next='A'
    for i in range(0,3):
        if chess[i][0]==chess[i][1] and chess[i][1]==chess[i][2] and chess[i][0]!=' ':
            if chess[i][0]=='X':
                result='A'
            else:
                result='B'
            break
    for j in range(0,3):
        if chess[0][j]==chess[1][j] and chess[1][j]==chess[2][j] and chess[0][j]!=' ':
            if chess[0][j]=='X':
                result='A'
            else:
                result='B'
            break
    if chess[0][0]==chess[1][1] and chess[1][1]==chess[2][2] and chess[0][0]!=' ':
        if chess[1][1]=='X':
            result='A'
        else:
            result='B'
    if chess[2][0]==chess[1][1] and chess[1][1]==chess[0][2] and chess[1][1]!=' ':
        if chess[1][1]=='X':
            result='A'
        else:
            result='B'
    if result!='Pending':
        break
if len(str)==18 and result=='Pending':
    result='Draw'
print(result)