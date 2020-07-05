def cross(p1, p2, p3):  # 叉积判定
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    return x1 * y2 - x2 * y1


def segment(p1, p2, p3, p4):  # 判断两线段是否相交
    # 矩形判定，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if (max(p1[0], p2[0]) >= min(p3[0], p4[0])  # 矩形1最右端大于矩形2最左端
            and max(p3[0], p4[0]) >= min(p1[0], p2[0])  # 矩形2最右端大于矩形1最左端
            and max(p1[1], p2[1]) >= min(p3[1], p4[1])  # 矩形1最高端大于矩形2最低端
            and max(p3[1], p4[1]) >= min(p1[1], p2[1])):  # 矩形2最高端大于矩形1最低端
        if (cross(p1, p2, p3) * cross(p1, p2, p4) <= 0
                and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0):
            D = 1
        else:
            D = 0
    else:
        D = 0
    return D

n=int(input())
for i in range(n):
    row1=[int(n) for n in input().split()]
    row2=[int(n) for n in input().split()]
    p1=[row1[0],row1[1]]
    p2=[row1[2],row1[3]]
    p3=[row2[0],row2[1]]
    p4=[row2[2],row2[3]]
    print(segment(p1,p2,p3,p4))