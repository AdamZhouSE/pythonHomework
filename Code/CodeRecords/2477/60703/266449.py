T = int(input())
for i in range(T):
    first = [int(x) for x in input().split(" ")]
    second = [int(x) for x in input().split(" ")]
    x1, y1, x2, y2 = first[0], first[1], first[2], first[3]
    x3, y3, x4, y4 = second[0], second[1], second[2], second[3]
    if (
            ((x1 < x3 and y1 < y3) and (x2 > x3 and y2 > y3)) or ((x1 < x4 and y1 < y4) and (x2 > x4 and y2 > y4))
        or ((x1 < x3 and y2 < y3) and (x2 > x3 and y1 > y3)) or ((x1 < x4 and y2 < y4) and (x2 > x4 and y1 > y4))

    ):
        print(1)
    else:
        print(0)