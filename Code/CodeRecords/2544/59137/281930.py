def s7():
    t = int(input())
    for i in range(t):
        s1 = input().split()
        s2 = input().split()

        x1 = float(s1[0])
        y1 = float(s1[1])
        x2 = float(s1[2])
        y2 = float(s1[3])

        x3 = float(s2[0])
        y3 = float(s2[1])
        x4 = float(s2[2])
        y4 = float(s2[3])

        s1_x = x2 - x1
        s1_y = y2 - y1
        s2_x = x4 - x3
        s2_y = y4 - y3

        if -s2_x * s1_y + s1_x * s2_y == 0:
            print(0)
            continue

        s = (-s1_y * (x1 - x3) + s1_x * (y1 - y3)) / (-s2_x * s1_y + s1_x * s2_y)
        t = (s2_x * (y1 - y3) - s2_y * (x1 - x3)) / (-s2_x * s1_y + s1_x * s2_y)

        if 0 <= s <= 1 and 0 <= t <= 1:
            print(1)
        else:
            print(0)


s7()