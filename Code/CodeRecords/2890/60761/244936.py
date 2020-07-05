n,x,y=map(int,input().split(" "))
positions=[]
temp=[]
times=0
for i in range(n):
    x1,y1=map(int,input().split(" "))
    positions.append([x1-x,y1-y])
for position in positions:
    if(position[0]==0):
        position[1]=1
    else:
        position[1]=format(position[1]/position[0],".6f")
        position[0]=1
for position in positions:
    if position not in temp:
        temp.append(position)
print(len(temp))