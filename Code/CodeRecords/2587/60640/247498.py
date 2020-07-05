"""
访问所有点的最小时间
尽量采取对角线走的方式，直到横纵坐标有相等的情况
"""
n = int(input())
inp = input().split(",")
x0, y0 = int(inp[0]), int(inp[1])
result = 0
for i in range(1, n):
    inp = input().split(",")
    x1, y1 = int(inp[0]), int(inp[1])
    # 斜线的的情况
    bias = min(abs(x1-x0), abs(y1-y0))
    # 直线的情况
    straight = max(abs(x1-x0), abs(y1-y0)) - bias
    # 更新坐标
    x0 = x1
    y0 = y1
    result += bias + straight
print(result)
