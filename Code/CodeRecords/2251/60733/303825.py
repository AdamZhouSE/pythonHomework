import itertools


def largestTriangleArea(points):
    def area(p, q, r):
        return .5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                        - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])

    return max(area(*triangle)
               for triangle in itertools.combinations(points, 3))

n =int(input())
points = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    l=list(map(int,input().split(",")))
    points[i][0]=l[0]
    points[i][1]=l[1]
res=largestTriangleArea(points)
print(res)