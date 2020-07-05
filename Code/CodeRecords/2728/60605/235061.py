# 题目描述
# 给定N个非负整数，其中每个代表坐标上的一个点（i，ai）。
#
# 绘制N条垂直线，使第i条线的两个端点位于（i，ai）和（i，0）。找到两条线，它们与x轴一起形成一个容器，以便该容器包含最多的水。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例都包含一个整数N，后跟N个以空格分隔的整数。
#
# 输出描述
# 对于每个测试用例，输出是表示可以包含的最大水面积的整数（使用2D时，最大面积而不是最大体积）

t = int(input())
li = []

for i in range(t):
    input()
    b = input().strip().split(" ")
    a = []
    for m in b:
        a.append(int(m))
    li.append(a)
# print(li)

for i in range(t):
    array = li[i]
    maxSizeTot = 0
    for index in range(len(array)):
        # 从某个点开始向左右
        cnt = 0
        maxHeight = 0
        maxSizeL = 0
        for j in range(index - 1, -1, -1):
            cnt += 1
            maxSizeL = max(maxSizeL, cnt*min(array[index], array[j]))
        cnt = 0
        maxHeight = 0
        maxSizeR = 0
        for j in range(index + 1, len(array)):
            cnt += 1
            maxSizeL = max(maxSizeL, cnt * min(array[index], array[j]))

        maxSizeTot = max(max(maxSizeL, maxSizeR), maxSizeTot)



    print(maxSizeTot)
