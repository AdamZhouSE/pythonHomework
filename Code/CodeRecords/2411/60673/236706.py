  
lenght = int(input())
coordinates = []
res = True
for i in range(lenght):
    coordinates.append(input())
x1 = coordinates[0][0:1]
x2 = coordinates[1][0:1]
y1 = coordinates[0][-1]
y2 = coordinates[1][-1]
if (x1==x2):
    for i in range(lenght):
        if (coordinates[i][0:1] != x1):
            res = False
            break
elif (y1 == y2):
    for i in range(lenght):
        if (coordinates[i][-1] != y1):
            res = False
            break
else:
    k = (int(y1) - int(y2)) / (int(x1) - int(x2))
    b = int(y2) - k * int(x2)
    for i in range(1, lenght):
        if (int(coordinates[i][-1]) != k * int(coordinates[i][0:1]) + b):
            res = False
            break
print (res)

