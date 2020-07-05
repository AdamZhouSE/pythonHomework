# S = |(x1 · y2 - x2 · y1) + (x2 · y3 - x3 · y2) + (x3 · y1 - x1 · y3)| / 2
n = int(input())
dots = []
for i in range(n):
    p = input().split(',')
    p = [int(x) for x in p]
    dots.append(p)
areas = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = abs((dots[i][0] * dots[j][1] - dots[j][0] * dots[i][1]) +
                       (dots[j][0] * dots[k][1] - dots[k][0] * dots[j][1]) +
                       (dots[k][0] * dots[i][1] - dots[i][0] * dots[k][1])) / 2
            areas.append(area)
print(max(areas))