from fractions import Fraction as F


def mirrorReflection(p, q):
    x = y = 0
    rx, ry = p, q
    targets = [(p, 0), (p, p), (0, p)]

    while (x, y) not in targets:
        t = float('inf')
        for v in [F(-x, rx), F(-y, ry), F(p - x, rx), F(p - y, ry)]:
            if v > 0: t = min(t, v)

        x += rx * t
        y += ry * t

        if x == p or x == 0:
            rx *= -1
        if y == p or y == 0:
            ry *= -1

    return 1 if x == y == p else 0 if x == p else 2


p = int(input())
q = int(input())
res = mirrorReflection(p, q)
print(res)
