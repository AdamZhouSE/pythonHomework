"""
判断一个点是否在矩形内部
即判断该点是否在上下和左右两条边之间
矩形四点为A,B,C,D
二维向量叉乘：x1y2 - x2y1 = |a||b|sin
如果夹角大于90，sin为负
如果该点在矩形外，则与对应两边夹角会有一个大于90
(AB X AE ) * (CD X CE)  >= 0 && (DA X DE ) * (BC X BE) >= 0
"""


class Point:
    x = 0
    y = 0

    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0


def get_across(p1, p2, p):
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)


def in_rectangle(p1, p2, p3, p4, p):
    res = get_across(p1, p2, p)*get_across(p3, p4, p) >= 0 and get_across(p2, p3, p)*get_across(p4, p1, p) >= 0
    return res


inp = input().split(" ")
n, d = int(inp[0]), int(inp[1])
a = Point(d, 0)
b = Point(n, n-d)
c = Point(n-d, n)
d = Point(0, d)
m = int(input())
for i in range(m):
    inp = input().split(" ")
    x, y = int(inp[0]), int(inp[1])
    e = Point(x, y)
    if in_rectangle(a, b, c, d, e):
        print("YES")
    else:
        print("NO")
