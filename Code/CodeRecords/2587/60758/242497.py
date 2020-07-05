num=int(input())
points=[]
for i in range(0,num):
    points.append(list(map(int,input().split(","))))
steps=0
for i in range(0,len(points)-1):
    x1=points[i][0]
    y1=points[i][1]
    x2=points[i+1][0]
    y2=points[i+1][1]
    steps+=max(abs(y2-y1),abs(x2-x1))
print(steps)