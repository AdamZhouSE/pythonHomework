num_points = int(input())
points = []
allnum = []
for i in range(num_points):
    points.append(str(input()).split(","))
for i in range(1, num_points):
    num = 0
    # 第一个点和之后每个点组成一条直线
    if (points[0][0] == points[i][0]):
        for j in range(num_points):
            if (points[0][0] == points[j][0]):
                num += 1
        allnum.append(num)

    else:
        k = (int(points[i][1]) - int(points[0][1])) / (int(points[i][0]) - int(points[0][0]))
        b = int(points[0][1]) - k * int(points[0][0])
        for j in range(num_points):
            if (int(points[j][1]) == k * int(points[j][0]) + b):
                num += 1
        allnum.append(num)
print (max(allnum))
