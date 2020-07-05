def minTimeToVisitAllPoints(points):
    list = []
    z = len(points)
    num = 0
    for i in range(z - 1):
        x = abs(points[i][0] - points[i + 1][0])
        y = abs(points[i][1] - points[i + 1][1])
        if x >= y:
            list.append(x)
        else:
            list.append(y)
    for n in list:
        num = num + n
    return num


if __name__ == '__main__':
    i = int(input())
    points = []
    for i in range(i):
        point = list(map(int, input().split(",")))
        points.append(point)
    print(minTimeToVisitAllPoints(points))
