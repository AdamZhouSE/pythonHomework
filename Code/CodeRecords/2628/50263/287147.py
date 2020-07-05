import math


def get_wide(a1, b1, a2, b2):
    count = 0
    if b1 == b2:
        count = abs(a1 - a2)
    elif a1 == a2:
        count = abs(b1 - b2)
    else:
        k = abs((a1-a2)/(b1-b2))
        for m in range(abs(a1-a2)):
            for j in range(abs(b1 - b2)):
                if k * m == j:
                    count += 1
    return count


n = int(input())
for i in range(n):
    l1 = input().split()
    l2 = input().split()
    l3 = input().split()
    x1, y1, x2, y2, x3, y3 = int(l1[0]), int(l1[1]), int(l2[0]), int(l2[1]), int(l3[0]), int(l3[1])
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    p = (a + b + c)/2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    wide = get_wide(x1, y1, x2, y2) + get_wide(x1, y1, x3, y3) + get_wide(x3, y3, x2, y2)
    result = int(s-wide/2 + 1.01)
    print(result)