def cutTree(position,cutpoint):
    if(len(position)==1):
        return 1
    if(len(cutpoint)==0):
        cutpoint.append(position[0][0])
        return 1+cutTree(position[1:],cutpoint)
    else:
        if(position[0][0]-position[0][1]>cutpoint[-1]):
            cutpoint.append(position[0][0])
            return 1+cutTree(position[1:],cutpoint)
        elif(position[0][0]+position[0][1]<position[1][0]):
            cutpoint.append(position[0][0]+position[0][1])
            return 1+cutTree(position[1:],cutpoint)
        else:
            cutpoint.append(position[0][0])
            return cutTree(position[1:],cutpoint)
t=int(input())
position=[]
for i in range(t):
    x,y=map(int,input().split(" "))
    position.append([x,y])
print(cutTree(position,[]))