n = int(input())
points = []
res = 0
for k in range(n):
    points.append([int(i) for i in input().split(',')])
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1 = points[i]
            x2,y2 = points[j]
            x3,y3 = points[k]
            tmp = 0.5*((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3))
            if tmp<0:
                tmp = -tmp
            if tmp>res:
                res = tmp
print(res)