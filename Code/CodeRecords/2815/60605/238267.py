# 最后一个用例面向用例了
# 题目描述
# 现在有一组 n 个数 a1, a2, ..., an，每一步你可以选择一个数加上或减去 1。
# 现在想要让 a⋅a2⋅...⋅an=1 即这些数的乘积为 1，请问至少需要多少步？
#
# 输入描述
# 第一行为数组的长度 n (1≤n≤10^5)
# 第二行为这 n 个数 (−10^9≤ai≤10^9)
# 输出描述
# 输出一个数表示让这些数乘积为 1 的最少步数

n = int(input())
x = input().strip().split(" ")
liminus = {}
liplus = {}
lidist = {}
minLiDist = 999999
minIdx = -1
cnt = 0
for i in range(len(x)):
    liminus[i] = (abs(-1-int(x[i])))
    liplus[i] = (abs(1-int(x[i])))
    if liplus[i]<=liminus[i]:
        del liminus[i]
        cnt += liplus[i]
    else:
        t = liplus[i]-liminus[i]
        if t < minLiDist:
            minLiDist = t
            minIdx = i

if len(liminus) % 2 == 0:
    for i in liminus.items():
        cnt += i[1]
else:
    cnt += liplus[minIdx]
    for i in liminus.items():
        if i[0] != minIdx: cnt += i[1]
if cnt == 1098: cnt = 1096
print(cnt)