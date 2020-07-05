n=int(input())
name=[]
points=[]
for i in range(n):
    line=input().split()
    name.append(line[0])
    points.append(int(line[1]))
names=list(set(name))
if names.__len__()==1:
    print(names[0])
else:
    point0=0
    point1=0
    for i in range(n):
        if name[i]==names[0]:
            point0+=points[i]
        else:
            point1+=points[i]
    if point0>point1:
        print(names[0])
    elif point0<point1:
        print(names[1])