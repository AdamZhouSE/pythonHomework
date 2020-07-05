def noncolinearPoints(coordinates):
    x_0 = coordinates[0][0]
    y_0 = coordinates[0][1]
    x_1 = coordinates[1][0]
    y_1 = coordinates[1][1]
    k = (y_0 - y_1) / (x_0 - x_1) if (x_0 != x_1) else 0
    b = y_0 - k * x_0
    x = coordinates[2][0]
    y = coordinates[2][1]
    if y != k * x + b:
        return "True"
    else:    
        return "False"

num = int(input())
coordinates = []
for i in range(num):
    coordinates.append(list(map(int,input().split(','))))
print(noncolinearPoints(coordinates))