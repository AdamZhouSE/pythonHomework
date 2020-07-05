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
for i in range(0,P):
    for j in range(i+1,P):
        length.append(leng(i,j))
        start.append(i)
        end.append(j)
lengt=length.copy()
n=0
while len(point)<P:
    min=findmin()
    if (start[min] in point and end[min] in point):
        length[min]=10000
        continue
    if start[min] not in point and end[min] not in point:
        temp=length[min]
        length[min]=10000
    else:
        n+=1
        if start[min] not in point:
            point.append(start[min])
        if end[min] not in point:
            point.append(end[min])
        newl.append(length[min])
        newp.append([start[min],end[min]])
        length[min]=10000
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
    if num>=0:
        del l[len(l)-1]
print(length)
print(newl)
print("{:.2f}".format(l[len(l)-1]))