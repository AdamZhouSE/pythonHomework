source=eval(input())
length=len(source)
playerone="A"
playertwo="B"
playerthree="Draw"
playerfour="Pending"
#target=""
rows=3
mostlength=9
def func(list0):
    maps= [[0 for i in range(rows)] for j in range(rows)]
    
    for i in range(length):
         if i%2==0:
            maps[list0[i][0]][list0[i][1]]=playerone
         else:
            maps[list0[i][0]][list0[i][1]]=playertwo
    if length%2==0:
        target=playertwo
    else:
        target=playerone
        
    for i in range(rows):
        if maps[i][0]==maps[i][1] and maps[i][0]==maps[i][2] and maps[i][0]!=0:
            return maps[i][0]
        if maps[0][i]==maps[1][i] and maps[0][i]==maps[2][i] and maps[0][i]!=0 :
            return maps[0][i]
    if maps[0][0]==maps[1][1] and maps[0][0]==maps[2][2] and maps[0][0]!=0:
        return maps[0][0]
    if maps[0][2]==maps[1][1] and maps[0][2]==maps[2][0] and maps[2][0]!=0:
        return maps[0][0]
    if length==mostlength:
        return playerthree
    return playerfour

print(func(source))
