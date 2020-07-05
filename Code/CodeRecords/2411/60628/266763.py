def colinearPoints(coordinates):
    x_0 = coordinates[0][0]
    y_0 = coordinates[0][1]
    x_1 = coordinates[1][0]
    y_1 = coordinates[1][1]
    k = (y_0 - y_1) / (x_0 - x_1) if (x_0 != x_1) else 0
    b = y_0 - k * x_0
    for i in range(3,len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        if y != k * x + b:
            return "False"
    return "True"

num = int(input())
coordinates = []
for i in range(num):
    coordinates.append(list(map(int,input().split(','))))
print(colinearPoints(coordinates))