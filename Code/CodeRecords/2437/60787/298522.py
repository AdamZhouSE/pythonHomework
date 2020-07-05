n,k=map(int,input().split())
wall=[0]
current=0
for step in range(0,n):
    temp=input().split()
    if temp[1]=="R":
        while len(wall)<current+int(temp[0]):
            wall.append(0)
        for i in range(current,current+int(temp[0])):
            wall[i]+=1
        current+=int(temp[0])
    else:
        while current-int(temp[0])<0:
            current+=1
            wall.insert(0,0)
        for i in range(current-1,current-int(temp[0])-1,-1):
            wall[i]+=1
        current-=int(temp[0])
re=0
for i in wall:
    if i>=k:
        re+=1
print(re)