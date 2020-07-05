b=input().lstrip("[").rstrip("]")+"],"
b=b.replace("[","")
b=b.split("],")
b.pop()
for mum,i in enumerate(b):
    temp=i.split(",")
    b[mum]=temp
c=[[0,0,0],[0,0,0],[0,0,0]]
tag=1;t=len(b)
for i in b:
    temp=i
    c[int(temp[0])][int(temp[1])]=tag
    tag*=-1
def winner(ele,t):
    x,y=0,0
    if(ele[0][0]+ele[1][1]+ele[2][2]==3) or ele[0][2]+ele[1][1]+ele[2][0]==3:
        return "A"
    elif ele[0][0]+ele[1][1]+ele[2][2]==-3 or ele[0][2]+ele[1][1]+ele[2][0]==-3:
        return "B"
    for i in range(3):
        if ele[i][0]+ele[i][1]+ele[i][2]==3:
            return "A"
        elif ele[i][0]+ele[i][1]+ele[i][2]==-3:
            return "B"
        elif ele[0][i]+ele[1][i]+ele[2][i]==3:
            return "A"
        elif ele[0][i]+ele[1][i]+ele[2][i]==-3:
            return "B"
    if(t==9):
        return "Draw"
    else:
        return "Pending"
print(winner(c,t))