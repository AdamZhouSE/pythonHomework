n = int(input())
coordinates = [[0] * 2] * n
for i in range(n):
    coordinates[i] = list(map(int, input().split(",")))
k = 0;
index = 0
is_line = True
for i in range(n - 1):
    xi = coordinates[i][0] - coordinates[i + 1][0]
    if xi != 0:
        k = xi
        index = i
        break
if k == 0:
    print(True)
else:
    k = (coordinates[index][1] - coordinates[index + 1][1]) / k
    for i in range(n):
        if i != index and i != index + 1:
            yi = coordinates[i][1] - coordinates[index][1]
            xi = coordinates[i][0] - coordinates[index][0]
            if yi != k * xi:
                is_line = False
                break
    print(is_line)
