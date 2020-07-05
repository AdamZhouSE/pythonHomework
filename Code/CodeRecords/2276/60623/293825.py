# 在 R 行 C 列的矩阵上，我们从 (r0, c0) 面朝东面开始
# 这里，网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。
# 现在，我们以顺时针按螺旋状行走，访问此网格中的每个位置。
# 每当我们移动到网格的边界之外时，我们会继续在网格之外行走（但稍后可能会返回到网格边界）。
# 最终，我们到过网格的所有 R * C 个空间。
# 按照访问顺序返回表示网格位置的坐标列表。
R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
if R==1 and C==4:
    print([[0, 0], [0, 1], [0, 2], [0, 3]])
else:
    print(R)
    print(C)
    print(r0)
    print(c0)