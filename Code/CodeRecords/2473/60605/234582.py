# 题目描述
# 在给定的直方图中找到最大的矩形区域，其中最大的矩形可以由许多连续的条形组成。为简单起见，假设所有条形都具有相同的宽度，并且宽度为1个单位。
#
# 输入描述
# 第一行包含一个整数“ T”，表示测试用例的总数。随后是T个测试用例。
# 在每个测试案例中，第一行都包含一个整数“ N”，表示数组的大小。
# 第二行包含N个以空格分隔的整数A1，A2，...，AN，它们表示数组的元素。数组的元素表示条形的高度。
#
# 输出描述
# 对于每个测试用例，在单独的一行中，连续条形可能的最大矩形区域。
import math
t = int(input())
liN = []
liArray = []
for i in range(t):
    liN.append(int(input()))
    b = []
    array = input().split(" ")
    for j in array:
        b.append(int(j))
    liArray.append(b)

for i in range(t):
    n = liN[i]
    array = liArray[i]
    maxSize = 0
    for index in range(0, n):
        totalHeight = array[index]
        thisHeight = array[index]
        for indexL in range(index-1, -1, -1):
            if array[indexL] >= thisHeight:
                totalHeight += thisHeight
            else:
                break
        for indexR in range(index+1, n):
            if array[indexR] >= thisHeight:
                totalHeight += thisHeight
            else:
                break
        maxSize = max(maxSize, totalHeight)
    print(maxSize)