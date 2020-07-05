import math
import sys


def execute(A, B, C, D, E, F, G, H):
    # 调整两个矩形位置, 让第一个矩形靠最左边
    if A > E:
        return execute(E, F, G, H, A, B, C, D)
    # 没有重叠的情况
    if B >= H or D <= F or C <= E:
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
    # 重叠情况
    # 下边界
    down = max(A, E)
    # 上
    up = min(C, G)
    # 左
    left = max(B, F)
    # 右
    right = min(D, H)
    return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

li = Input[0].split(",")

A = int(li[0])
B = int(li[1])
C = int(li[2])
D = int(li[3])
E = int(li[4])
F = int(li[5])
G = int(li[6])
H = int(li[7])


print(execute(A,B,C,D,E,F,G,H))
