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
        k = 10 ** 10
        b = k * (y0*x - y*x0) / (y - y0)
    else:
        k = (y - y0) / (x - x0)
        b = (y0*x - y*x0) / (x - x0)
    for i in range(1, len(points)):
        if i >= len(points):
            break
        xt = points[i][0]
        yt = points[i][1]
        if k * xt + b - yt < 10 ** -10 :
            del(points[i])
    del(points[0])
    count += 1
print(count)
