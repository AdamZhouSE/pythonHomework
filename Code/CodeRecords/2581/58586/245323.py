ghosts=int(input())
res=[]
for i in range(ghosts):
    res.append(list(map(int,input().split(","))))
target=list(map(int,input().split(",")))
def getDis(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])
escape_dis=getDis([0,0],target)
flag=True
for i in range(ghosts):
    temp=getDis(res[i],target)
    if temp<=escape_dis:
        flag=False
        break
print(flag)