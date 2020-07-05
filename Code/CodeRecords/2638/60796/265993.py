import math
ns=input().split(" ")
N=int(ns[0])
M=int(ns[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
instruct=[]
for i in range(M):
    instruct.append(input().split(" "))
    j = 0
    while j < len(instruct[i]):
        instruct[i][j] = int(instruct[i][j])
        j = j + 1
#print(ls)
#print(instruct)
result=[]
for i in range(len(instruct)):
    #print(instruct[i])
    if instruct[i][0]==1:
        x=instruct[i][1]-1
        y=instruct[i][2]-1
        k=instruct[i][3]
        for j in range(x,y+1):
            ls[j]=ls[j]+k
    elif instruct[i][0]==2:
        x = instruct[i][1] - 1
        y = instruct[i][2] - 1
        this=0
        for j in range(x,y+1):
            this=this+ls[j]
        result.append(this/(y+1-x))
    elif instruct[i][0]==3:
        x = instruct[i][1] - 1
        y = instruct[i][2] - 1
        this = 0
        for j in range(x, y + 1):
            this = this + ls[j]
        average=this / (y+1-x)
        this=0
        for j in range(x,y+1):
            this=this+pow(ls[j]-average,2)
        result.append(this/(y+1-x))

for i in range(len(result)):
    print("%.4f"%result[i])

