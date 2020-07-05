"""
4x+4y+4z = P
2xy + 2yz + 2xz = S
求xyz的最大值

可以观察得出
要使体积最大，有两条边相等，设为x=y
最后得到方程
6x^2 - px + S = 0
取小的那个解
"""
import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    P, S = int(inp[0]), int(inp[1])
    length = (P-math.sqrt(P*P-24*S))/12
    height = P/4 - 2*length
    res = length*length*height
    print("%.5lf" % res)
