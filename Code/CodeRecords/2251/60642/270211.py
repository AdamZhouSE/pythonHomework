def triangleArea(a,b,c):
    area = 0
    area =  (a[0]*b[1]-b[0]*a[1])+(b[0]*c[1]-c[0]*b[1])+(c[0]*a[1]-a[0]*c[1])/2
    return area

times = int(input())
points = []
for i in range(times):
    points.append([int(i) for i in input().split(',')])
maxarea = 0
for i in range(len(points)):
    for j in range(i,len(points)):
        for k in range(j,len(points)):
            maxarea=max(maxarea,triangleArea(points[i],points[j],points[k]))
print(maxarea)