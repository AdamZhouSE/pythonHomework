import functools


def sortPoints(p1, p2):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] == p2[0]:
        if p1[1] < p2[1]:
            return -1
    return 1


N, K = [int(x) for x in input().split()]
points = []
for i in range(N):
    points.append([int(x) for x in input().split()])
points.sort(key=functools.cmp_to_key(sortPoints))
# print(points)
overlap = []
for i in range(0, N):
    for j in range(i+1, N):
        if abs(points[i][0] - points[j][0]) < K and abs(points[i][1] - points[j][1]) < K:
            if len(overlap) != 0:
                print(-1)
                exit()
            overlap.append((K - abs(points[i][0] - points[j][0])) * (K - abs(points[i][1] - points[j][1])))
if len(overlap) != 0:
    print(overlap[0])
else:
    print(0)