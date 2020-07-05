num_points = int(input())
points = []
allnum = []
for i in range(num_points):
    points.append(str(input()).split(","))
for k in range(num_points):
    for i in range(num_points):
        if(k==i):
            continue
        num = 1
        if (points[k][0] == points[i][0]):
            for j in range(num_points):
                if(j==i):
                    continue
                if (points[k][0] == points[j][0]):
                    num += 1
            allnum.append(num)

        else:
            k2 = (int(points[i][1]) - int(points[k][1])) / (int(points[i][0]) - int(points[k][0]))
            b = int(points[k][1]) - k2 * int(points[k][0])
            for j in range(1,num_points):
                if(j==i):
                    continue
                if (int(points[j][1]) == int(k2) * int(points[j][0]) + int(b)):
                    num += 1
            allnum.append(num)
print (max(allnum))
