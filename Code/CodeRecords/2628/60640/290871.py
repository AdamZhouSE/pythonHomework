"""
皮克定理
S = a + b/2 -1
S是三角形面积，a是内点，b是边界点个数
a = S + 1 - b/2
求三角形面积S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2
求两点线段间的坐标个数 b = gcd(abs(x1-x2), abs(y1-y2))
"""
import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    x1, y1 = int(inp[0]), int(inp[1])
    inp1 = input().split(" ")
    x2, y2 = int(inp1[0]), int(inp1[1])
    inp2 = input().split(" ")
    x3, y3 = int(inp2[0]), int(inp2[1])
    S = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)//2
    b12 = math.gcd(abs(x1-x2), abs(y1-y2))
    b13 = math.gcd(abs(x1-x3), abs(y1-y3))
    b23 = math.gcd(abs(x2-x3), abs(y2-y3))
    b = b12 + b13 + b23
    res = S + 1 - b//2
    print(res)
