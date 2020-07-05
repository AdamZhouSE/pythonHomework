import itertools

n = int(input())
points = []
for i in range(n):
    points.append([])
for i in range(n):
    temp = input()
    points[i].append(int(temp[0]))
    points[i].append(int(temp[2]))

EPS = 1e-7
points = set(map(tuple, points))

ans = float('inf')
for p1, p2, p3 in itertools.permutations(points, 3):
    p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
    if p4 in points:
        v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
        v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
        if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
            area = abs(v21) * abs(v31)
            if area < ans:
                ans = area

print('%.4f' %ans) if ans < float('inf') else print('%.4f' %0)
