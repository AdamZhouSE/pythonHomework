def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

points = []
for i in range(4):
    points.append(tuple([int(x) for x in input().split(",")]))
points.sort()
print(dist(points[0], points[1]) != 0 and dist(points[0], points[1]) == dist(points[1], points[3])  == dist(points[3], points[2]) == dist(points[2], points[0])   and dist(points[0],points[3])==dist(points[1],points[2]))