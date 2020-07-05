n=int(input())
xy=[[0]*2]*n
for i in range(0,n):
    xy[i]=[int(k) for k in input().split(',')]

k=(xy[0][1]-xy[1][1])/(xy[0][0]-xy[1][0])
b=xy[0][1]-k*xy[0][0]
re=1
for i in range(1,n):
    if xy[i][0]-xy[0][0]!=0:
        if (xy[i][1]-xy[0][1])/(xy[i][0]-xy[0][0])==k and b==xy[i][1]-k*xy[i][0]:
            re+=1
xlist=[i[0] for i in xy]
x=xlist.count(xy[0][0])
ylist=[i[1] for i in xy]
for i in range(0,n):
    if xlist.count(xy[i][0])>x:
        x=xlist.count(xy[i][0])
y=ylist.count(xy[0][1])
for i in range(0,n):
    if ylist.count(xy[i][1])>y:
        y=ylist.count(xy[i][1])
if max(x,y)>re:
    print(max(x,y))
else:
    print(re)
    