nk = input().split(" ")
n, k = int(nk[0]), int(nk[1])
cnt = 0
points = []
for i in range(n):
    p = input().split(" ")
    points.append(list(map(int, p)))
cnt, p1, p2 = 0, 0, 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (points[j][0] < (points[i][0] + k)) and (points[j][0] > (points[i][0] - k)):
            if (points[j][1] < (points[i][1] + k)) and (points[j][1] > (points[i][1] - k)):
                cnt += 1;
                p1, p2 = i, j
if cnt == 0:
    print(0)
elif cnt == 1:
    area = (k-abs(points[p1][0] - points[p2][0])) * (k-abs(points[p1][1] - points[p2][1]))
    print(area)
else:
    print(-1)
