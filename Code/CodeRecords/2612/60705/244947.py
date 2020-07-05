import math


def Manhatton(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def euclid(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)


n = int(input())
for i in range(0, n):
    number_of_points = int(input())
    points = []
    for j in range(0, number_of_points):
        position = list(map(int, input().split(" ")))
        points.append([position[0], position[1]])

    count = 0
    for k in range(0, number_of_points-1):
        for l in range(k+1, number_of_points):
            if Manhatton(points[k], points[l]) == euclid(points[k], points[l]):
                count += 1
    print(count)
    if count == 1:
        print(points)
