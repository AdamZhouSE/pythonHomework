def func():
    points_num = int(input())
    points = []
    i = 0
    while i < points_num:
        points.append([int(x) for x in input().split(",")])
        i += 1

    x_s = 0
    y_s = 0
    i = 0
    while i < len(points) - 1:
        x_s += abs(points[i + 1][0] - points[i][0])
        y_s += abs(points[i + 1][1] - points[i][1])
        i += 1

    print(max(x_s, y_s))


func()
