num=int(input())
points=[]
for i in range(num):
    points.append([int(x) for x in input().split(',')])
judge=True
if (points[1][1]-points[0][1])!=0:
    rate=(points[1][0]-points[0][0])/(points[1][1]-points[0][1])
    for i in range(1,len(points)-1):
        if points[i+1][1]-points[i][1]==0:
            judge=False
            break
        if(points[i+1][0]-points[i][0])/(points[i+1][1]-points[i][1])!=rate:
            judge=False
            break
else:
    for i in range(1,len(points)-1):
        if(points[i+1][1]-points[i][1])!=0:
            judge=False
            break
print(judge)