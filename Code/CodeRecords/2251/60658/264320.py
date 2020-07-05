def area(a,b,c):
    return 0.5 * abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[1]*b[0]-b[1]*c[0]-c[1]*a[0])

n = int(input())
points  =[]
for i in range(n):
    points.append([int(x) for x in input().split(",")])
m = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            m = max(m,area(points[i],points[j],points[k]))
print(m)