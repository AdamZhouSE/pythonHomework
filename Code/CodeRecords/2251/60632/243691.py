import math


def triangle(a, b, c):
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area


def length(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    return math.sqrt(x*x + y*y)


n = int(input())
points = []
area = 0
for i in range(n):
    points.append(list(map(float, input().split(','))))
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            x = length(points[i], points[j])
            y = length(points[i], points[k])
            z = length(points[j], points[k])
            tmp = triangle(x,y,z)
            if tmp > area:
                area = tmp
print('{0:.1f}'.format(area))
