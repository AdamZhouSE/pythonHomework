# a=input().replace("[","").rstrip("]")+"],"
# a=a.split("],")
# a.pop()
# b=[]
q=input()
a=[]
for i in range(int(q)):
    a.append(input())
b=[]
for i in a:
    temp=i.split(",")
    b.append([int(x) for x in temp])
position=[[-1,0],[0,1],[1,0],[0,-1]]
def getHeight(x,y):
    if x<0 or x>=len(b) or y<0 or y>=len(b[0]):
        return 0
    else:
        return b[x][y]
count=0
for i in range(len(b)):
    for j in range(len(b[0])):
        if(b[i][j]>0):
            count+=2
        for k in range(4):
            xi=i+position[k][0]
            yi=j+position[k][1]
            temp=b[i][j]-getHeight(xi,yi)
            if(temp>0):
                count+=temp
print(count)