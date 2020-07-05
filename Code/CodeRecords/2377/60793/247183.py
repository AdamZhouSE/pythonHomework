point_num = int(input())
points = []
result = True
for i in range(0, point_num):
    points.append(list(map(int, input().split(","))))
for i in range(1, point_num - 1):
    tan1 = (points[i][0] - points[i][1]) / (points[i - 1][0] - points[i - 1][1])
    tan2 = (points[i + 1][0] - points[i + 1][1]) / (points[i][0] - points[i][1])
    if tan1 == tan2:
        result = False
print(result)