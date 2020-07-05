line=input().split()
line=[int(x) for x in line]
times=line[0]
sideLen=line[1]
centers=[]
limit=[0 for i in range(4)]
for i in range(times):
    line=input().split()
    line=[int(x)*2 for x in line]
    if line[0]-sideLen<limit[2]:
        limit[2]=line[0]-sideLen
    if line[0]+sideLen>limit[0]:
        limit[0]=line[0]+sideLen
    if line[1]-sideLen<limit[1]:
        limit[1]=line[1]-sideLen
    if line[1]+sideLen>limit[3]:
        limit[3]=line[1]+sideLen
    centers.append(line)
xyPlane=[[0 for j in range(limit[3]-limit[1])]for i in range(limit[0]-limit[2])]


for i in centers:
    for j in range(i[0]-sideLen-limit[2],i[0]+sideLen-limit[2]):
        for k in range(i[1]-sideLen-limit[1],i[1]+sideLen-limit[1]):

            xyPlane[j][k]+=1
answer=0
s=0
for i in xyPlane:
    for j in i:
        if j==2:
            answer=1
            s+=1
        if j>2:
            answer=-1
            break
if answer==1:
    print(s//4)
else:
    print(answer)