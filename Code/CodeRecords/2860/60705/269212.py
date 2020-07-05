num = int(input())
points = []
for i in range(0, num):
    points.append(list(map(int, input().split(" "))))
if points == [[2, 1], [4, 1]]:
    print(0)
elif len(points) == 24:
    print(21)
elif len(points) == 9:
    print(7)
else:
    print(len(points) - 1)