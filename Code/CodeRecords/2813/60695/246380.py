n = int(input())
name = []
point = [0] * n
maxPoint = 0
for i in range(0, n):
    a = input().split(" ")
    if a[0] not in name:
        name.append(a[0])
    ind = name.index(a[0])
    point[ind] += int(a[1])
    if point[ind] > maxPoint:
        maxPoint = point[ind]
        winner = a[0]
print(winner)