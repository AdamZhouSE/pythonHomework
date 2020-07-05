import itertools
def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def isRectangle(p1, p2, p3, p4):
    x_c = (p1[0] + p2[0] + p3[0] + p4[0])/4
    y_c = (p1[1] + p2[1] + p3[1] + p4[1])/4
    d1 = distance(p1, (x_c,y_c))
    d2 = distance(p2, (x_c,y_c))
    d3 = distance(p3, (x_c,y_c))
    d4 = distance(p4, (x_c,y_c))
    return d1 == d2 and d1 == d3 and d1 == d4

def rectangleArea(p1, p2, p3, p4):
    vertex = [p1, p2, p3, p4]
    dis = []
    for i in range(3):
        dis.append(distance(vertex[i],p4))
    dis.sort()
    return (dis[0]*dis[1])**0.5

def minRectangle(points):
    points = set(map(tuple, points))
    res = float('inf')
    for p1, p2, p3, p4 in itertools.combinations(points, 4):
        if isRectangle(p1, p2, p3, p4):
            area = rectangleArea(p1, p2, p3, p4)
            if area < res:
                res = area
    return res if res != float('inf') else 0

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split(','))))
print(("%.4f" % minRectangle(points)))