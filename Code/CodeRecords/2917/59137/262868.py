def s26():
    n = int(input())
    points = []
    for i in range(n):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        points.append([x, y])

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                count = count + 1
    print(count)


s26()