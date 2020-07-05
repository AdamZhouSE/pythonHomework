def maxcolinearPoints(coordinates):
    res = 0
    for i in range(0,len(coordinates)):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        for j in range(0,len(coordinates)):
            x2 = coordinates[j][0]
            y2 = coordinates[j][1]
            if x1 == x2 and y1 == y2:
                continue
            count = 0
            for k in range(0,len(coordinates)):
                x = coordinates[k][0]
                y = coordinates[k][1]
                if (y2-y1)*(x-x2) == (x2-x1)*(y-y2):
                    count += 1
            res = max(res,count)
    return res

num = int(input())
coordinates = []
for i in range(num):
    coordinates.append(list(map(int,input().split(','))))
print(maxcolinearPoints(coordinates))