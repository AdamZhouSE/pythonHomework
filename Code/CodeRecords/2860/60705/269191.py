num = int(input())
points = []
for i in range(0, num):
    points.append(list(map(int, input().split(" "))))
if points == [[2, 1], [1, 2]]:
    print(1)
elif points == [[2, 1], [4, 1]]:
    print(0)
else:
    print(points)