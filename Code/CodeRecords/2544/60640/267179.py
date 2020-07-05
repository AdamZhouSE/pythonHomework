"""
两个直线相交即不平行，斜率不等
(y2-y1)(x4-x3) - (x2-x1)(y4-y3) != 0

两条线段相交AB CD
跨立实验
如果两线段相交，那么一条线段的两个端点必然在另一条线段的两侧
AB在线段CD的两侧，CD在线段AB的两侧
(AC叉乘AB）* （AD叉乘AB）<= 0
(CA叉乘CD）* （CB叉乘CD）<= 0
"""
t = int(input())
for i in range(t):
    inp1 = input().split(" ")
    x1, y1, x2, y2 = int(inp1[0]), int(inp1[1]), int(inp1[2]), int(inp1[3])
    inp2 = input().split(" ")
    x3, y3, x4, y4 = int(inp2[0]), int(inp2[1]), int(inp2[2]), int(inp2[3])
    ac_ab = (x3-x1)*(y2-y1) - (x2-x1)*(y3-y1)
    ad_ab = (x4-x1)*(y2-y1) - (x2-x1)*(y4-y1)
    ca_cd = (x1-x3)*(y4-y3) - (x4-x3)*(y1-y3)
    cb_cd = (x2-x3)*(y4-y3) - (y2-y3)*(x4-x3)
    if ca_cd*cb_cd <= 0 and ac_ab*ad_ab <= 0:
        print(1)
    else:
        print(0)
