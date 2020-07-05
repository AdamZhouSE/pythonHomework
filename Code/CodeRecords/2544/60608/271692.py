def cross(p1: list, p2: list, p3: list):  # 跨立实验
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    return x1 * y2 - x2 * y1


def func7():
    for _ in range(0, eval(input())):
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        p1, p2, p3, p4 = a1[0:2], a1[2:], a2[0:2], a2[2:]

        if (max(p1[0], p2[0]) >= min(p3[0], p4[0])
                and max(p3[0], p4[0]) >= min(p1[0], p2[0])
                and max(p1[1], p2[1]) >= min(p3[1], p4[1])
                and max(p3[1], p4[1]) >= min(p1[1], p2[1])):
            if cross(p1, p2, p3) * cross(p1, p2, p4) <= 0 and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0:
                print(1)
            else:
                print(0)
        else:
            print(0)


func7()
