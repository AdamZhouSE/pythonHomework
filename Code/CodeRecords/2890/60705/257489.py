line1 = list(map(int, input().split(" ")))
num_of_terrorism = line1[0]
x0 = line1[1]
y0 = line1[2]
points = []
for i in range(num_of_terrorism):
    line = list(map(int, input().split(" ")))
    points.append([line[0], line[1]])

count = 0
while len(points) > 0:
    point = points[0]
    x = point[0]
    y = point[1]
    if x == x0:
        i = 1
        while i < len(points):
            xt = points[i][0]
            if xt == x:
                del(points[i])
                i -= 1
            i += 1
    else:
        k = (y - y0) / (x - x0)
        b = (y0*x - y*x0) / (x - x0)
        i = 1
        while i < len(points):
            xt = points[i][0]
            yt = points[i][1]
            if (k * xt + b - yt) < (10 ** -5):
                del(points[i])
                i -= 1
            i += 1
    del(points[0])
    count += 1
print(count)
