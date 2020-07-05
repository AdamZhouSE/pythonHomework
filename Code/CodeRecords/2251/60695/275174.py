n = int(input())
point = [[0] * 2 for i in range(n)]
for i in range(0, n):
    p = input().split(",")
    point[i][0] = int(p[0])
    point[i][1] = int(p[1])
areas = []
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            areas.append(0.5 * (abs(
                (point[i][0] - point[j][0]) * (point[i][1] - point[k][1])) + abs((point[k][0] - point[i][0]) * (
                    point[i][1] - point[j][1]))))
areas = sorted(areas)
print(areas[len(areas) - 1])