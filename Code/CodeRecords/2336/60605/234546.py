# 题目描述
# 给定一个数组A和一个整数K。找到大小为K的每个连续子数组的最大值。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例的第一行包含一个整数N，它表示数组的大小和子数组K的大小。
# 第二行包含N个以空格分隔的整数A1，A2，...，AN，它表示数组的元素。
#
# 输出描述
# 打印大小为k的每个子数组的最大值。

t = int(input())
liN = []
liK = []
liArray = []
for i in range(t):
    a = input().split()
    liN.append(int(a[0]))
    liK.append(int(a[1]))
    a = input().split()
    b = []
    for j in a:
        b.append(int(j))
    liArray.append(b)

for i in range(t):
    n = liN[i]
    k = liK[i]
    array = liArray[i]
    repeat = n-k+1
    for j in range(n-k+1):
        max = 0
        for t in range(j, j+k):
            if array[t] > max: max = array[t]
        print(max, end=" ")
    print()