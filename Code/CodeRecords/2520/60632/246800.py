def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
points = [[x, y] for x in range(0, R) for y in range(0, C)]  # 各点坐标
p0 = [r0, c0]
result = []
for i in range(0, R + C - 1):
    for j in points:
        if distance(p0, j) == i:
            result.append(j)
print(result)
