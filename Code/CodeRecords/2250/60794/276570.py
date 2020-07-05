num = int(input())
coordinates = []
ans = []
for i in range(num):
    coordinates.append([])
    a = input().split(",")
    coordinates[i].append(int(a[0]))
    coordinates[i].append(int(a[1]))
for i in range(num):
    for j in range(i+1, num):
        if coordinates[i][0] - coordinates[j][0] == 0:
            k = 0
        else:
            k = (coordinates[i][1] - coordinates[j][1])/(coordinates[i][0] - coordinates[j][0])
        h = coordinates[i][1] - k * coordinates[i][0]
        z = 0
        for l in range(num):
            if coordinates[l][1] == k * coordinates[l][0] + h:
                z = z + 1
        ans.append(z)
print(max(ans))