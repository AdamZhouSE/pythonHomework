c, n = map(int, input().split(" "))
coordinates = []
for i in range(0, n):
    x, y = map(int, input().split(" "))
    coordinates.append((x, y))
coordinates = sorted(coordinates, key=lambda x: x[0])
another_coordinates = sorted(coordinates, key=lambda x: x[1])
result = max(coordinates[n - 1][0] - coordinates[0][0] + 1,
             another_coordinates[n - 1][1] - another_coordinates[0][1] + 1)
for i in range(0, n - c + 1):
    another_coordinates = sorted(coordinates[i:i+c], key=lambda x:x[1])
    temp = max(coordinates[i + c - 1][0] - coordinates[i][0] + 1,
               another_coordinates[c - 1][1] - another_coordinates[0][1] + 1)
    result = min(result, temp)
print(result)
