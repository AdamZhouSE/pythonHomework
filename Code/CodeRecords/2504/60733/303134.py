def kClosest(points, K):
    a = lambda x: x[0] ** 2 + x[1] ** 2
    points.sort(key=a)
    return points[:K]

s = input().replace(",", " ").replace("[", "").replace("]", "")
l = list(s.split())
length = len(l)
move = [[0 for i in range(2)] for j in range(length//2)]
k=int(input())
for i in range(0, length, 2):
    move[i // 2][0] = int(l[i])
    move[i // 2][1] = int(l[i + 1])
res = kClosest(move,k)
print(res)