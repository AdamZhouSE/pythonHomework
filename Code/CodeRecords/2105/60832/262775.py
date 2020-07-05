coordinate = list(map(int, input().split(',')))

x1 = coordinate[0]
y1 = coordinate[1]

x2 = coordinate[2]
y2 = coordinate[3]

x3 = coordinate[4]
y3 = coordinate[5]

x4 = coordinate[6]
y4 = coordinate[7]

A = (x2 - x1) * (y2 - y1)
B = (x4 - x3) * (y4 - y3)

a = min(x2, x4) - max(x1, x3)
b = min(y2, y4) - max(y1, y3)

AWithB = a * b

ans = A + B - AWithB

print(ans)
