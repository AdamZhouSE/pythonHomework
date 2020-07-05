T = int(input())
N = int(input())
for i in range(0, T):
    points = []
    for j in range(0, N):
        points.append(input().split(" "))
    num = 0
    for a in range(0, len(points) - 1):
        for b in range(a + 1, len(points)):
            if points[a]==points[b]:continue
            man_distance = abs(float(points[a][0]) - float(points[b][0])) + abs(float(points[a][1]) - float(points[b][1]))
            ou_distance = pow((pow((float(points[a][0]) - float(points[b][0])), 2) + pow((float(points[a][1]) - float(points[b][1])), 2)), 0.5)
            if man_distance==ou_distance:
                num+=1
    print(0)