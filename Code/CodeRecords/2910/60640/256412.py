"""
2.26
旋转矩形
要使得高度单调递减
使得前一个的高度最大，
"""
n = int(input())
data = []
for i in range(n):
    inp = list(map(int, input().split(" ")))
    data.append(inp)
max_h = max(data[0][0], data[0][1])
isLower = True
for i in range(1, n):
    max_h1 = max(data[i][0], data[i][1])
    min_h1 = min(data[i][0], data[i][1])
    # 如果w1，h1都小于h0，则h0更新为w1与h1的最大值
    if max_h1 <= max_h:
        max_h = max_h1
    # 如果w1，h1中有一个小于h0，则h0更新为那个值
    elif min_h1 <= max_h:
        max_h = min_h1
    else:
        isLower = False
if isLower:
    print("YES")
else:
    print("NO")
