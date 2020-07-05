def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] + b[1])


R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
points = [[x, y] for x in range(0, R) for y in range(0, C)]
p0 = [r0, c0]
dis = [distance(x, p0) for x in points]
match = dict(zip(dis, points))
dis = sorted(dis)
result = [match[x] for x in dis]
print(result)
