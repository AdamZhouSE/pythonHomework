n = int(input())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def judge(aa, bb, cc, dd):
    if max(aa.x, bb.x) < min(cc.x, dd.x):
        return False
    if max(aa.y, bb.y) < min(cc.y, dd.y):
        return False
    if max(cc.x, dd.x) < min(aa.x, bb.x):
        return False
    if max(cc.y, dd.y) < min(aa.y, bb.y):
        return False
    if mult(aa, cc, bb) * mult(aa, bb, dd) < 0:
        return False  # // 正确的话也就是aa, bb要在cc或者dd的两边
    if mult(cc, aa, dd) * mult(cc, dd, bb) < 0:
        return False
    return True


def mult(p0, p1, p2):
    return (p0.x - p1.x) * (p0.y - p2.y) - (p0.y - p1.y) * (p0.x - p2.x);


for i in range(n):
    x = input()
    y = input()
    x = [int(j) for j in x.split(" ")]
    y = [int(j) for j in y.split(" ")]
    aa = Point(x[0], x[1])
    bb = Point(x[2], x[3])
    cc = Point(y[0], y[1])
    dd = Point(y[2], y[3])
    test = judge(aa, bb, cc, dd)
    if test:
        print(1)
    else:
        print(0)
