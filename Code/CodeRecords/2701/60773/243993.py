def isWin(l):
    #print(l)
    if l[0][0]==l[0][1] and l[0][1]==l[0][2] and l[0][0]!=0:
        return True
    elif l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][0]!=0:
        return True
    elif l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][0]!=0:
        return True
    elif l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]!=0:
        return True
    elif l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[0][1]!=0:
        return True
    elif l[0][2]==l[1][2] and l[1][2]==l[2][2] and l[0][2]!=0:
        return True
    elif l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[0][0]!=0:
        return True
    elif l[0][2]==l[1][1] and l[1][1]==l[2][0] and l[1][1]!=0:
        return True
    else:
        return False
s=input()

board=[[0,0,0],[0,0,0],[0,0,0]]
step=s[2:len(s)-2].split("],[")
#print(board)
#print(step)
result=""
for i in range(0,len(step),2):
    #print(int(step[i][0]))
    #print(int(step[i][2]))
    board[int(step[i][0])][int(step[i][2])]='x'
    if(isWin(board)):
        result='A'
        break
    if(i+1<len(step)):
        board[int(step[i+1][0])][int(step[i+1][2])] = 'o'
        if (isWin(board)):
            result = 'B'
            break
if result=="" :
    if len(step)==9:
        result="Draw"
    else:
        result="Pending"
print(result)
