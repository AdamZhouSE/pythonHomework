nums=int(input())
points=[]
for i in range(nums):
    line=list(map(int,input().split(",")))
    points.append(line)
start=points[0]
path=0
for i in range(1,nums):
    row=abs(points[i][0]-start[0])
    col=abs(points[i][1]-start[1])
    start=points[i]
    path+=max(row,col)
print(path)