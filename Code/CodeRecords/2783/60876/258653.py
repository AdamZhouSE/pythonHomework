n=int(input())
list=[]
names=[]
points=[]
winners=[]
sequence=[]
for i in range(0,n):
    name,num=input().split(" ")
    point=int(num)
    list.append([name,point])
    if name not in names:
        names.append(name)
        points.append(0)
for item in list:
    ind=names.index(item[0])
    points[ind]+=item[1]
    item[1]=points[ind]
max=points[0]
for point in points:
    if point>max:
        max=point
while max in points:
    ind=points.index(max)
    winners.append(names[ind])
    points[ind]=0
for item in list:
    if (item[0] in winners) and item[1]>=max:
        print(item[0])
        break