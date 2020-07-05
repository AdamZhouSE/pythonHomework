import math


def m(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def o(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split(" "))))
    # print(points)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if abs(m(points[i], points[j]) - o(points[i], points[j])) < 10**-10:
                count += 1
    print(count)