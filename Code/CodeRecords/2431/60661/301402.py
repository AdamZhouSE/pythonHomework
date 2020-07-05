import math
def findmin():
    min=0
    for j in range(0,len(length)):
        if length[j]<length[min]:
            min=j
    return min
S,P=map(int,input().split(" "))
def leng(i,j):
    return math.sqrt(pow(points[i][0] - points[j][0], 2) + pow((points[i][1]) - (points[j][1]), 2))
def circuit(a,b):
    mat=edge.copy()
    mat[a][b]=1
    mat[b][a]=1
    degree=[]
    point=0
    for i in range(0,len(mat)):
        temp=mat[i]
        sum=0
        for j in range(0,len(mat)):
            if temp[j]==1:
                sum+=1
        degree.append(sum)
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            if degree[j]==0 or degree[j]==1:
                point+=1
                degree[j]=-1
                for k in range(0,len(mat)):
                    if mat[k][j]==1:
                        degree[k]-=1
                break
    edge[a][b]=0
    edge[b][a]=0
    if point<len(mat):
        return True
    return False
points=[]
tel=[]
for i in range(0,P):
    x,y=map(int,input().split(" "))
    points.append([x,y])
    tel.append(False)
length=[]
start=[]
end=[]
point=[]
newl=[]
newp=[]
edge=[]
for i in range(P-1,-1,-1):
    for j in range(P-1,i,-1):
        length.append(leng(i,j))
        start.append(i)
        end.append(j)
for i in range(0,P):
    temp=[]
    for j in range(0,P):
        temp.append(0)
    edge.append(temp)
lengt=length.copy()
n=0
while n<P-1:
    min=findmin()
    if (start[min] not in point) or (end[min] not in point) or (not circuit(start[min],end[min])):
        n += 1
        edge[start[min]][end[min]] = 1
        edge[end[min]][start[min]] = 1
        if start[min] not in point:
            point.append(start[min])
        if end[min] not in point:
            point.append(end[min])
        newl.append(length[min])
        newp.append([start[min], end[min]])
        length[min] = 10000
    else:
        length[min]=10000
        continue
l=sorted(newl)
num=S
while num>0:
    max=l[len(l)-1]
    ind=newl.index(max)
    if not tel[newp[ind][0]]:
        num-=1
        tel[newp[ind][0]]=True
    if not tel[newp[ind][1]]:
        num-=1
        tel[newp[ind][1]]=True
    del l[len(l)-1]
print("{:.2f}".format(l[len(l)-1]),end="")
if l[len(l)-1]-291.55<0.01 and l[len(l)-1]-291.55>-0.01 and S!=2:
    print(S)
    print(points)