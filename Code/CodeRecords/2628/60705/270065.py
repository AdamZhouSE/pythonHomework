def area(x1, y1, x2, y2, x3, y3):
    return abs(
        (1/2) * (
            x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)
        )
    )


if __name__ == '__main__':
    tests = int(input())
    for test in range(0, tests):
        [x1, y1] = list(map(int, input().split(" ")))
        [x2, y2] = list(map(int, input().split(" ")))
        [x3, y3] = list(map(int, input().split(" ")))
        Sabc = area(x1, y1, x2, y2, x3, y3)
        minx = min(x1, x2, x3)
        maxx = max(x1, x2, x3)
        miny = min(y1, y2, y3)
        maxy = max(y1, y2, y3)
        count = 0
        for i in range(minx+1, maxx):
            for j in range(miny+1, maxy):
                if abs(area(i, j, x2, y2, x3, y3) +
                       area(x1, y1, i, j, x3, y3) +
                       area(x1, y1, x2, y2, i, j) - Sabc) < 10**-3\
                        and area(i, j, x2, y2, x3, y3) > 0 \
                        and area(x1, y1, i, j, x3, y3) \
                        and area(x1, y1, x2, y2, i, j) > 0:
                    count += 1
        print(count)
