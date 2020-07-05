def checkStraightLine(c: list) -> bool:
    return all((x - c[0][0]) * (y - c[1][1]) == (x - c[1][0]) * (y - c[0][1]) for x, y in c[2:])

points = []
n = eval(input())
for i in range(n):
    points.append(list(map(int,input().split(','))))
print(checkStraightLine(points))