num = int(input())
coordinates = []
for i in range(num):
    coordinates.append([])
    a = input().split(",")
    coordinates[i].append(int(a[0]))
    coordinates[i].append(int(a[1]))
k = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0] - coordinates[1][0])
h = coordinates[0][1] - k * coordinates[0][0]
x = 1
for i in range(num):
    if coordinates[i][1] != k * coordinates[i][0] + h:
        x = 0
        break
if x == 0:
    print("False")
else:
    print("True")